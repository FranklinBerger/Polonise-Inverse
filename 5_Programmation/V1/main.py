# Parametres d'execution
from CONSTANTES import *

doc="""
Fichier: main.py
Projet: Calculatrice Polonaise Inversse V0.5
Verssion & Date: V1 15.08.2020

Dependances:

Description:


Contenu:


Auteur·e:
- Sleny Martinez (MAS)
- XXX XXX
"""


""" ------ Imports ------ """
# Augmentation de l'optimisation a la compilation
import micropython
micropython.opt_level(3)
# Gestion des exceptions etendue en cas de debug
if DEBUG_MODE_MAIN: micropython.alloc_emergency_exception_buf(128)

# Imports bibliotheques interne
import machine
import time

# Imports bibliotheques externe officielle (lib)


# Imports bibliotheques externe maisons
import Clavier
import Clavier_RPN
import RPN
import PCF8574
import LCD_RPN
import LCD_2004




""" ------ Code Utile ------ """
" --- Initialisation --- "

LCD_RPN.init()

" --- Systeme --- "


while True:
    # Ne fait quelque-chose que si une touche a ete pressee, sinon rien
    if Clavier_RPN.haveToAct():

        # Affiche les erreurs dans le REPL si en debug
        if DEBUG_MODE_MAIN:
            print("--- Actions")
            try:
                Clavier_RPN.exec()
            except Exception as e:
                hasError = True
                print("ERREUR D'ACTION:\n" + str(e))
            else:
                hasError = False
            LCD_RPN.showRPN(error = hasError)
        else:
            # On fait une recuperation d'erreur ici car les fonctions de la RPN en on pas
            try:
                Clavier_RPN.exec()
            except:
                hasError = True
            else:
                hasError = False
            # On affiche la RPN a l'ecrant
            LCD_RPN.showRPN(error = hasError)
    else:
        pass
