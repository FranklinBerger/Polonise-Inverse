# CONSTANTES & PARAMETRES
import micropython
DEBUG_MODE = micropython.const(True)

doc="""
Fichier: main.py
Projet: Calculatrice Polonaise Inversse V0.5
Verssion & Date: V1 15.08.2020

Dependances:
- PCF8574.py

Description:


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

