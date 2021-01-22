# Parametres d'execution
from CONSTANTES import *

doc=
"""
Fichier: RPN.py
Projet: Calculatrice Polonaise Inversse V0.5
Verssion & Date: V1 05.08.2020

Description:
Systeme de calcul sous format RPN (Polonaise inversse)
La pile est de 4 niveaux (X, Y, Z, T) avec duplication sur le niveau T
Des systemes de gestion de la pile (rotation, ecriture des niveaux, etc...)
sont contenu ainsi que de nombreuses fonctions mathematiques communes
Tous les nombres sont contenu au format flotant decimal. On pourra les
recuperer sous ce format via getXfloat() ou arrondi sans perte via getX()

Contenu:


Auteur·e:
- Sleny Martinez (MAS)
- XXX XXX
"""


""" ------ Imports ------ """
# Gestion des exceptions etendue en cas de debug
import micropython
if DEBUG_MODE : micropython.alloc_emergency_exception_buf(128) 

# Imports bibliotheques interne
import machine

# Imports bibliotheques externe officielle (lib)
# Imports bibliotheques externe maisons


""" ------ Code Utile ------ """
" --- Initialisation --- "

" --- Systeme --- "

def fonction ( param ):
    global doc
    doc+="""
    Fonction: fonction ( param )
    Description
    """
    return None



""" ------ Algoritme de presentation ------ """
if __name__ == "__main__":
    # Affichage doc du fichier
    print(doc)
