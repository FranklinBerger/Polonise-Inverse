# CONSTANTES & PARAMETRES
import micropython
DEBUG_MODE = micropython.const(False)

doc="""
Fichier: Clavier.py
Projet: Calculatrice Polonaise Inversse V0.5
Verssion & Date: V1 15.08.2020

Dependances:

Description:
Gestion d'un clavier par matrice
Les colonnes sont controlees au travers de sortie en
open-collector (peuvent etre drivees par PNP en saturation) et
en logique positive
Le clavier est analyse par balayage des colonnes (step) et lecture des lignes (=> frame)
Ce balayage se fait en continu au travrs d'un thread (peut etre desactive et reactiver)
Chaque pression de touche est enregistree dans un buffer a recuperer
Les pressions sont enregistrees sous le format d'une liste [ligne, colonne]
P.Ex: [4:0] coresspond a une pression de la touche a la cinquieme ligne et premiere colonne


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
import _thread

# Imports bibliotheques externe officielle (lib)
# Imports bibliotheques externe maisons




""" ------ Code Utile ------ """
" --- Initialisation --- "
# col: liste de chaque pin en colonne
# sous la forme [numero_colonne , objet_pin]
# row: liste de chaque pin en ligne
# sous la forme [numero_ligne , objet_pin, memoire_etat]
# memoire_etat estr la pour detecter les flanc montant (pression touche)
_col = []
_row = []
_mem =  []
_bufferKey = []
_threadRun = False
_threadID = None
_delayFrame = 0
_delayStep = 0

def init (col, row, delayFrame = 3, delayStep = 3):
    """
    Fonction: init (col, row, delayFrame = 50, delayStep = 5)
    Initialisation du clavier
    col & row: liste contenant les N° GPIOs de chaque pin (dans l'ordre)
    """
    global _col, _row, _mem, _threadRun, _delayFrame, _delayStep, _mem_k
    _delayFrame = delayFrame
    _delayStep = delayStep

    # Initialisation lignes
    index = 0
    row_mem = []
    for r in row:
        _row.append([ index, machine.Pin(r,mode=machine.Pin.IN,pull=machine.Pin.PULL_DOWN) ])
        #row_mem.append(index + 1)
        index += 1
    # Initialisation colonnes
    index = 0
    for c in col:
        # value = 1 : colonne desactivee
        # On met un pull-up car sur certains GPIO (notament 12 et 13), le courant de fuite
        # de l'open-drain suffit à mettre le transistor en saturation
        _col.append([ index, machine.Pin(c,mode=machine.Pin.OPEN_DRAIN,value=1,pull=machine.Pin.PULL_UP) ])
        #_mem.append(row_mem)
        index += 1

    # Initialisation memoire pour anti-doublon
    # /!\ Si on fait [[0] * len(_row)] * len(_col), on se retrouve avec des sous-listes
    # liees entre elles (a tester pour voir le resultat)
    _mem = [[0] * len(_row) for _ in range(len(_col))]

    # Lance le thread de lecture du clavier
    setThread(True)


def _startThread ():
    """
    Fonction: _startThread ()
    Lance via le module _thread le thread de lecture du clavier
    """
    _thread.start_new_thread(_threadClavier, [])


" --- Systeme --- "
def _threadClavier (arg=None):
    """
    Fonction: threadClavier (arg=None)
    Thread de lecture en continu du clavier
    """
    global _col, _row, _threadRun, _delayFrame, _delayStep, _bufferKey

    # Jusqu'a ce qu'on arete le thread
    while _threadRun:
        # Balayage Colonne
        for c in _col:
            # Activation colonne et stabilisation HW
            c[1].value(0)
            time.sleep_ms(_delayStep)
            # Lecture lignes
            for r in _row:
                #print("r: " + str(r) + " C: " + str(c) + " => " + str(_row_mem[c[0]][r[0]]))
                r_val = r[1].value()
                r_Oval = _mem[c[0]][r[0]]
                if r[0]==0 and c[0]==4 and DEBUG_MODE:
                    None
                    # print("...")
                    # print("C: " + str(c[0]) + " : " + str(_mem[c[0]]))
                    # print(r_val)
                    # print(r_Oval)
                # Test flanc montant par XOR
                if r_val == True and r_val ^ r_Oval:
                    # Enregistrement pression dans buffer
                    _bufferKey.append([ r[0] , c[0] ])
                # Enregistrement valeur pour suite (anti-doublon)
                _mem[c[0]][r[0]] = r_val
            # Desactivation colonne
            c[1].value(1)
        # Fin frame, delais
        time.sleep_ms(_delayFrame)


def setThread (run):
    """
    Fonction: setThread (run)
    Arete / lance le thread de lecture du clavier
    Fonction utilisat·eur·rice
    """
    global _threadRun, _threadID
    if run and _threadRun == False:
        _threadRun = True
        if not DEBUG_MODE:
            _startThread ()
        else:
            raise Exception("Le thread Clavier n'as pas ete lance car le systeme Clavier est en mode debug")
    else:
        _threadRun = False

def readBuffer (nKey = None, remove = True):
    """
    Fonction: readBuffer ()
    Renvoie le buffer contenant les touches pressees et vide ce dernier
    nKey = Nombre de touches max a extraire
    remove = Faut-il supprimer les touches lues? (De base oui)
    """
    global _bufferKey
    # Contre index out of range
    #print("---")
    #print("nKey : " + str(nKey))
    #print("bufferKey : " + str(_bufferKey))
    nKey = nKey if nKey != None and nKey <= len(_bufferKey) else len(_bufferKey)
    k = _bufferKey[: nKey]
    if remove:
        _bufferKey = _bufferKey[nKey if nKey != None else len(_bufferKey) :]
    return k

def clearBuffer ():
    """
    Fonction:clearBuffer ()
    Vide le buffer
    """
    global _bufferKey
    _bufferKey = []

def any ():
    """
    Fonction: any ()
    Renvoie le nombre de touches dans le buffer
    """
    global _bufferKey
    return len(_bufferKey)


""" ------ Algoritme de presentation ------ """
if __name__ == "__main__":
    # Affichage doc du fichier
    print(doc)
