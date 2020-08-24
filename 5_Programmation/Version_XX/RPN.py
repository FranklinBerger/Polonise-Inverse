# CONSTANTES & PARAMETRES
import micropython
DEBUG_MODE = micropython.const(True)

doc="""
Fichier: RPN.py
Projet: Calculatrice Polonaise Inversse V0.5
Verssion & Date: V1 05.08.2020

Description:
Systeme de calcul sous format RPN (Polonaise inversse)
La pile est de 4 niveaux (X, Y, Z, T) avec duplication sur le niveau T
Des systemes de gestion de la pile (rotation, ecriture des niveaux, etc...)
sont contenu ainsi que de nombreuses fonctions mathematiques communes
Tous les nombres sont contenu au format flotant decimal. On pourra les
recuperer sous ce format via get ( layer ) ou arrondi sans perte via getInt( layer )
Gestion aussi de l'ecriture d'une valleur X via 

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
import math

# Imports bibliotheques externe officielle (lib)
# Imports bibliotheques externe maisons




""" ------ Code Utile ------ """
" --- Initialisation --- "
# Initialisation des niveaux de la pile
# TrueX definit si le X actuel est vrais ou seulement
# la persistence d'afichage apres un ENT
# Ceci permet de dupliquer X si plusieurs ENT a la suite
_pile = {
    "X" : "0" ,
    "Y" : 0.0 ,
    "Z" : 0.0 ,
    "T" : 0.0 ,
    "TrueX" : False
}

" --- Systeme --- "
# --- Controle des niveaux de la pile
# Definit pour N = X, Y, Z et T:
# - set ( layer , val )
# - get ( layer )
# - getInt ( layer )

def getPile ():
    """
    Fonction: getPile ()
    Return la valleur la pile tel qu'elle est
    """
    global _pile
    return _pile

def set ( layer , val ):
    """
    Fonction: set ( layer , val )  
    Modifie la valleur de l'etage layer de la pile
    """
    global _pile
    _pile[layer] = float( val ) if layer in "XYZT" else val

def get ( layer ):
    """
    Fonction: get ()
    Return la valleur la pile au niveau layer en float
    """
    return float( getPile()[layer] )

def getInt ( layer ):
    """
    Fonction: getInt ()
    Return la valleur layer de la pile
    Si valleur ronde, la rend int, sinon la rend float
    """
    _pileL = get(layer)
    return int(_pileL) if int(_pileL) == _pileL else _pileL


# --- Ecriture de X
def _setX ( val ):
    """
    Fonction: setX ( val )  
    Modifie la valleur de X en brut
    """
    global _pile
    _pile["X"] = val

def _getX ():
    """
    Fonction: getX ()  
    Obtient la valeur de X en brut
    """
    global _pile
    return _pile["X"]
    
def writeX ( char ):
    """
    Fonction: writeX ( char )
    Ecriture de X
    Le caractere doit etre 0-9 ou .
    """
    # Si TrueX a False (X = affichage), reecrit sur une base brut
    _setX( _getX() + char if get("TrueX") else char )
    set("TrueX", True)


# --- Actions sur la pile ---
def shiftUp ():
    """
    Fonction: shiftUp ()
    Equivalent de la fonction ENT
    Fait monter la pile d'un etage => libere la couche X
    A ne pas confondre avec rotateUp
    La valleur T sera perdue
    """
    set("T" , get("Z") )
    set("Z" , get("Y") )
    set("Y" , get("X") )
    set("TrueX" , False )

def shiftDown ():
    """
    Fonction: shiftDown ()
    Fait descendre la pile d'un etage
    A ne pas confondre avec rotateDown
    La valleur X sera perdue
    La valleur T sera doublee dans Z
    """
    set("X" , get("Y") )
    set("Y" , get("Z") )
    set("Z" , get("T") )
    set("TrueX" , False )
    












""" ------ Algoritme de presentation ------ """
if __name__ == "__main__":
    # Affichage doc du fichier
    print(doc)
