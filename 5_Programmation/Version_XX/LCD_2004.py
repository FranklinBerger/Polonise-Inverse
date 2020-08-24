# CONSTANTES & PARAMETRES
import micropython
DEBUG_MODE = micropython.const(True)

doc="""
Fichier: LCD_2004.py
Projet: Calculatrice Polonaise Inversse V0.5
Verssion & Date: V1 15.08.2020

Dependances:
- PCF8574.py

Description:
Gestion d'affichage sur ecrant LCD 20x4 au travers d'un IO Extender PCF8574 et
avec gestion de la luminosite de la backlight de l'ecrant (via PWM @ 1[KHz])
Les pins E (Enable) et RS (Commande Data / Instruction) sont controlees en directe,
la pin R/W (Ecriture / Lecture) est maintenue en lecture (GND)
Le systeme fonctionne sous la forme d'un buffer (tableau 20x4) suivi d'un rafraichissement
de l'ecrant.

Contenu:


Auteur·e:
- Sleny Martinez (MAS)
- XXX XXX
"""


""" ------ Imports ------ """
# Gestion des exceptions etendue en cas de debug
if DEBUG_MODE: micropython.alloc_emergency_exception_buf(128) 

# Imports bibliotheques interne
import machine
import time

# Imports bibliotheques externe officielle (lib)


# Imports bibliotheques externe maisons
import PCF8574




""" ------ Code Utile ------ """
" --- Initialisation --- "
_RS = None
_E = None
_BL = None
#_BL_PWM = None
_PCF_D = None

_LCD_buffer = {
1 : "                    " , # Ligne 1
2 : "                    " , # Ligne 2
3 : "                    " , # Ligne 3
4 : "                    "   # Ligne 4
}

def init (RS, E, BL, PCF8574):
    """
    Fonction: init (RS, E, BL, I2C)
    Definit les pins a utiliser (objet Pin ou I2C)
    """
    global _RS, _E, _BL, _PCF_D#, _BL_PWM
    _RS = RS
    _E = E
    _BL = BL
    #_BL_PWM = machine.PWM(_BL, freq=1000, duty=1023) if _BL != None else None
    _PCF_D = PCF8574
    
    # Procedure d'initialisation selon datasheet
    _E.value(1)
    time.sleep_ms(100)
    _send(0, 0x30)
    time.sleep_ms(5)
    _send(0, 0x30)
    time.sleep_us(200)
    _send(0, 0x30)
    time.sleep_us(200)
    _send(0, 0x38)
    _send(0, 0x10)
    _showDisplay()
    _send(0, 0x06)
    
    # Vidage Ecrant => Pret a commencer
    clearDisplay()


" --- Systeme --- "

def _send (RS, Datas):
    """
    Fonction: send (RS, D)
    Envoie des informations selon RS et Datas
    Gere l'application des Datas par I2C, de RS en
    directe et du flanc descendant de E
    """
    global _RS, _E, _BL, _PCF_D#, _BL_PWM
    
    # Envoi des donnes par I2C
    _PCF_D.write(Datas)
    # Application RS
    _RS.value(RS)
    # Mise a 1 de E (pour flanc descendant)
    _E.value(1)
    # Delais d'integration par l'ecrant
    time.sleep_us(1)
    # Validation des informations (flanc descendant E)
    _E.value(0)
    # Delais d'integration par l'ecrant
    time.sleep_us(1)
    

def _showDisplay (C = False, B = False):
    """
    Fonction: _showDisplay (C = False, B = False)
    Allume l'ecrant
    Si C = True, le curseur sera visible
    Si B = True, le curseur clignottera
    De base, curseur invisible
    """
    data = 0x0C
    data = data + 0x2 if C is True else data
    data = data + 0x1 if B is True else data
    _send(0, data)


def _shiftCursor ():
    """
    Fonction: _shiftCursor ()
    Fait que le curseur se decale (pas l'ecrant) et
    que le tout s'ecrive de gauche a droite (ecriture latine)
    """
    _send(0, 0x14)




""" --- Actions ecrant pour utilisat·eur·rice """
def setBacklight (value):
    """
    Fonction: setBacklight (value = 100)
    Definit la luminosite du backlight, la valleur est True ou False
    """
    #global _BL_PWM
    #_BL_PWM.duty(int(value * 10.23))
    
    global _BL
    # Value: False => BL allume, True => BL eteint
    _BL.value(not value)

def getBuffer ():
    """
    Fonction: getBuffer ()
    Renvoie l'etat actuel du buffer
    """
    global _LCD_buffer
    return _LCD_buffer

def setBuffer (buffer):
    """
    Fonction: setBuffer ()
    Recois le nouvel etat du buffer
    Si ne corespond pas a une liste de 4 string de 20 caracteres,
    renvoie une erreur
    """
    global _LCD_buffer
    
    if type(buffer) != dict or \
    len(buffer) != 4 or \
    len(buffer[1]) != 20 or \
    len(buffer[2]) != 20 or \
    len(buffer[3]) != 20 or \
    len(buffer[4]) != 20:
        raise Exception("Donnees invalide, une liste de 4 string de 20 caracteres est requise.")
    else:
        _LCD_buffer = buffer

def setLine (line, text):
    """
    Fonction: setLine ()
    Modifie une ligne de l'ecrant
    Le texte doit faire au maximum 20 caracteres
    """
    buffer = getBuffer()
    buffer[line] = text + ((20 - len(text)) * " ") if len(text) <= 20 and type(text) == str else ""
    if buffer[line] == "": raise Exception("text doit etre un string de maximum 20 carateres de long.")
    setBuffer(buffer)

def setChar (line, pos, char):
    """
    Fonction: setChar ()
    Modifie le caracter a la ligne line et au rang pos, definit a char
    """
    global _LCD_buffer
    # On fait +1 pour que le premier char soit le N°1
    _LCD_buffer[line][pos + 1] = char

def writeChar (char):
    """
    Fonction: _write_char (char)
    Ecrit un caracter a l'ecrant
    """
    _send(1, _getCharCGROMadress(char))

def clearDisplay ():
    """
    Fonction: clear_display ()
    Efface l'ecrant et met le curseur au debut
    """
    _send(0, 0x01)
    time.sleep_ms(2)

def fetch ():
    """
    Fonction: fetch ()
    Envoie le buffer a l'ecrant
    """
    # On commence par effacer totalement l'ecrant
    clearDisplay()
    
    # Puis on ecrit chaque char l'un apres l'autre
    # On doit faire dans l'ordre des lignes 1, 3, 2, 4 car
    # le curseur fait ce trajet (ref. au datasheet)
    for i in [1, 3, 2, 4]:
        for c in getBuffer()[i]:
            writeChar(c)
    





""" ------ Base de donnees ------ """
# CGROM, mappage de la ROM interne de l'ecrant contenant les caracteres
# le rang du caractere permet de definir l'adresse interne de celui-ci
# Ex: CGROM.index("A") returnera 65 (0x41) ce qui est l'adresse interne
# Chaque ligne est 16 caracteres soit l'exploitation d'un nible faible
# pour nible fort constant (voir commentaires)
# Note: tous les caracteres (natament les symboles speciaux) n'ont pas ete
# ajoutes (voir a partir de 0x8X) parce que j'avais la flemme
CGROM = micropython.const(
"""□□□□□□□□□□□□□□□□""" + # 0x0X
"""□□□□□□□□□□□□□□□□""" + # 0x1X 
""" !"#$%&'()*+,-./""" + # 0x2X 
"""0123456789:;<=>?""" + # 0x3X 
"""@ABCDEFGHIJKLMNO""" + # 0x4X 
"""PQRSTUVWXYZ[¥]^_""" + # 0x5X
"""`abcdefghijklmno""" + # 0x6X
"""pqrstuvwxyz{|}→←""" + # 0x7X
"""□□□□□□□□□□□□□□□□‎‎""" + # 0x8X
"""□□□□□□□□□□□□□□□□‎‎""" + # 0x9X
"""□□□□□·□□□□□□□□□□""" + # 0xAX
"""□□□□□□□□□□□□□□□□""" + # 0xBX
"""□□□□□□□□□□□□□□□□""" + # 0xCX
"""□□□□□□□□□□□□□□□□""" + # 0xDX
"""□□□□□□□□□□□□□□□□""" + # 0xEX
"""□□□□□□□□□□□□□□□□‎"""   # 0xFX
)

def _getCharCGROMadress (char):
    """
    Fonction: _getCharCGROMadress (char)
    Renvoie l'adresse de la CGROM d'un caracter determiner,
    soit la valleur à écrire dans la CGRAM
    Convertis dirrectement le tout en string binaire pour
    simplifier l'ecriture I2C par la suite
    """
    try:
        index = CGROM.index(str(char))
    except Exception:
        raise Exception("Caracter " + char + " inconnu ou invalide.")
    else:
        return index




""" ------ Algoritme de presentation ------ """
if __name__ == "__main__":
    # Affichage doc du fichier
    print(doc)

