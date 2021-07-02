# Parametres d'execution
from CONSTANTES import *

doc="""
Fichier: LCD_2004.py
Projet: Calculatrice Polonaise Inversse V0.5
Verssion & Date: V1 15.08.2020

Dependances:
- LCD_2004.py

Description:
Module endemique au projet de Calculatrice en polonaise inversse
Gestion d'affichage sur l'ecrant de la pile RPN et des divers affichages annexe
Voir fonction showRPN

Contenu:


Auteur·e:
- Sleny Martinez (MAS)
- XXX XXX
"""


""" ------ Imports ------ """
# Gestion des exceptions etendue en cas de debug
import micropython
if DEBUG_MODE_LCD: micropython.alloc_emergency_exception_buf(128)

# Imports bibliotheques interne
import machine
import time

# Imports bibliotheques externe officielle (lib)

# Imports bibliotheques externe maisons
import RPN
import Clavier_RPN
import PCF8574
import LCD_2004
import CONSTANTES



""" ------ Code Utile ------ """
" --- Initialisation --- "
# --- Initialisation LCD2004A
# Initialisation pin directes
pin_BL_LCD = machine.Pin(5, mode = machine.Pin.OPEN_DRAIN)
pin_RS_LCD = machine.Pin(26, mode = machine.Pin.OUT)
pin_E_LCD = machine.Pin(27, mode = machine.Pin.OUT)
# Initialisation I2C pour Data
i2c_LCD_PCF8574 = machine.I2C(0, scl=machine.Pin(32), sda=machine.Pin(33))
lcd_PCF8574 = PCF8574.PCF8574(i2c_LCD_PCF8574)
# Initialisation Ecrant
LCD_2004.init(
    pin_RS_LCD,
    pin_E_LCD,
    pin_BL_LCD,
    lcd_PCF8574)

def init():
    create2ndChar()

    # Ouverture sypmathique
    LCD_2004.writeLine(CONSTANTES.START_TEXT[0]) # Ligne 1
    LCD_2004.writeLine(CONSTANTES.START_TEXT[2]) # Ligne 2
    LCD_2004.writeLine(CONSTANTES.START_TEXT[1]) # Ligne 3
    LCD_2004.writeLine("Loading", full = False) # Ligne 4 puis ...
    for i in range(20 - len("Loading")):
        LCD_2004.writeChar(".")
        time.sleep_ms(150)

    # Affichage 0 de la RPN
    showRPN()

" --- Systeme --- "
def showRPN(error = False):
    """
    Fonction: showRPN()
    Affiche a l'ecrant le necessaire de la RPN.
    Va chercher seul les informations souhaitees
    """
    # recuperation toute pille RPN
    pileRPN = RPN.getPile()
    # Set une ligne a la fois
    LCD_2004.setLine(1, "T:" + str(pileRPN["T"])[:18] )
    LCD_2004.setLine(2, "Z:" + str(pileRPN["Z"])[:18] )
    LCD_2004.setLine(3, "Y:" + str(pileRPN["Y"])[:18] )
    LCD_2004.setLine(4, "X:" + str(pileRPN["X"])[:18] )
    # Ajouts
    # Cas de la touche 2nd activee
    if Clavier_RPN.get2nd():
        LCD_2004.setChar(1, 20, "\xff")
    # Cas d'une erreur
    if error:
        LCD_2004.setLine(4, "X:ERROR")
    # Refresh l'ecrant
    LCD_2004.fetch()

    # Debug
    if DEBUG_MODE_LCD:
        print("""Affichage Pile:
T: """ + str(pileRPN["T"])[:18] + """
Z: """ + str(pileRPN["Z"])[:18] + """
Y: """ + str(pileRPN["Y"])[:18] + """
X: """ + str(pileRPN["X"])[:18] + """
2nd: """ + str(Clavier_RPN.get2nd()) + """
ERROR: """ + str(error) )

def create2ndChar():
    LCD_2004._send(0, 0x40) # CGRAM caracter 1
    LCD_2004._send(1, 0b00011001) # ##..#
    LCD_2004._send(1, 0b00010101) # #.#.#
    LCD_2004._send(1, 0b00010011) # #..##
    LCD_2004._send(1, 0b00000000) # .....
    LCD_2004._send(1, 0b00011110) # ####.
    LCD_2004._send(1, 0b00010001) # #...#
    LCD_2004._send(1, 0b00010001) # #...#
    LCD_2004._send(1, 0b00011110) # ####.
    LCD_2004.setCursorPos(1,1) # Retour au debut de l'ecrant


""" ------ Algoritme de presentation ------ """
if __name__ == "__main__":
    # Affichage doc du fichier
    print(doc)
