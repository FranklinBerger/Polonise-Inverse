# CONSTANTES & PARAMETRES
import micropython
DEBUG_MODE = micropython.const(False)

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
#import mpmath

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
    "TrueX" : False ,
    "AfterEnt" : False ,
    "LastX" : 0
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
    try:
        return float( getPile()[layer] )
    except Exception:
        return int( getPile()[layer] )

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
    # Si apres "Ent", on doit aire un shift up avant ecriture pour ne pas
    # supprimer notre resultat
    if get("AfterEnt"):
        shiftUp()
        set("AfterEnt", False)
    # Si TrueX a False (X = affichage), reecrit sur une base brut
    _setX( _getX() + char if get("TrueX") else char )
    set("TrueX", True)

def _actOnXY (newX):
    """
    Fonction: _actOnXY (newX)
    "Ecrase" Y dans X, X = newX
    """
    set("Y", newX)
    shiftDown()
    set("AfterEnt", True)

# --- Actions sur la pile ---
def swapXY ():
    """
    Fonction: swapXY ()
    Echange les valeurs de X et Y
    """
    oldX = get("X")
    set("X", get("Y"))
    set("Y", oldX)

def shiftUp ():
    """
    Fonction: shiftUp ()
    Equivalent de la fonction ENT
    Fait monter la pile d'un etage => libere la couche X
    A ne pas confondre avec rotateUp
    La valleur T sera perdue
    Enreistre la veleur dans LastX
    """
    set("T" , get("Z") )
    set("Z" , get("Y") )
    set("Y" , get("X") )
    set("LastX", get("X"))
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
    set("TrueX" , True )

def rotateUp ():
    """
    Fonction: rotateUp ()
    Fait tourner la le vers le haut
    A ne pas confondre avec shiftUp()
    """
    oldT = get("T")
    shiftUp()
    set("X", oldT)

def rotateDown ():
    """
    Fonction: rotateDown ()
    Fait tourner la le vers le bas
    A ne pas confondre avec shiftDown()
    """
    oldX = get("X")
    shiftDown()
    set("T", oldX)

def clear ():
    """
    Fonction: clear ()
    Remet toutes les valeurs de la pile a 0
    """
    global _pile
    _pile = {
        "X" : "0" ,
        "Y" : 0.0 ,
        "Z" : 0.0 ,
        "T" : 0.0 ,
        "TrueX" : False ,
        "AfterEnt" : False
    }

def lastX ():
    """
    Fonction: lastX ()
    Remet la derniere valeur de X entree (par shiftUp) dans X
    """
    set("X", get("LastX"))

def delX ():
    """
    Fonction: delX ()
    Supprime un caractere de X
    Si plus rien, met a 0
    Si X est un chiffre valide (p.ex apres addition), remet a 0
    """
    _setX( _getX()[:-1] if type(_getX()) == str and len(_getX()) > 1 else "0" )
    set("TrueX", False if _getX() == "0" else True)

def clearX ():
    """
    Fonction: clearX ()
    Met X a 0
    """
    _setX("0")
    set("TrueX", False)

# --- Actions mathematique ---
def opposite ():
    """
    Fonction: opposite ()
    Y + X
    """
    _setX(-get("X"))

def invert ():
    """
    1 / X
    """
    _setX( 1 / get("X"))

def add ():
    """
    Fonction: add ()
    Y + X
    """
    _actOnXY(get("Y") + get("X"))

def sigma ():
    """
    Fonction: sigma ()
    X = somme de tous les x de x a 1
    P.ex: sigma de 5 = 5+4+3+2+1 = 15
    On la calcul par f(x) = (x * (x+1)) / 2
    """
    x = get("X")
    _setX( ((x+1) * x) / 2 )

def subtract ():
    """
    Fonction: sub ()
    Y - X
    """
    _actOnXY(get("Y") - get("X"))

def round ():
    """
    Fonction: round ()
    X = round(X)
    """
    _setX( float( int( get("X") ) ) )

def multiply ():
    """
    Fonction: multiply ()
    Y * X
    """
    _actOnXY(get("Y") * get("X"))

def factorial ():
    """
    Fonction: factorial ()
    X = X!
    """
    x = 1
    for i in range(get("X"), 1, -1): x *= i
    _setX( x )

def divide ():
    """
    Fonction: add ()
    Y / X
    """
    _actOnXY(get("Y") / get("X"))

def modulo ():
    """
    Fonction: add ()
    Y % X
    """
    _actOnXY(get("Y") % get("X"))

def pi ():
    """
    Fonction: pi ()
    X = pi (3.141593)
    """
    _setX(math.pi)

def e ():
    """
    Fonction: e ()
    X = e (2.718282)
    """
    _setX(math.e)

def square ():
    """
    Fonction: square ()
    X = X^2
    """
    _setX( math.pow( get("X") , 2 ) )

def square_root ():
    """
    Fonction: square_root ()
    X = racine carree de X
    """
    _setX( math.pow( get("X") , (1/2) ) )

def power_to ():
    """
    Fonction: power_to ()
    X = Y^X
    """
    _actOnXY( math.pow( get("Y") , get("X") ) )

def root ():
    """
    Fonction: square_root ()
    X = racine Xeme de Y
    """
    _actOnXY( math.pow( get("Y") , (1/get("X")) ) )

def e_pow_x ():
    """
    Fonction: e_pow_x ()
    X = e ^ X
    """
    set("X" , math.pow( math.e , get("X") ) )

def ten_pow_x ():
    """
    Fonction: ten_pow_x ()
    X = 10 ^ X
    """
    set("X" , math.pow( 10 , get("X") ) )

def log ():
    """
    Fonction: log ()
    X = log10(X)
    """
    _setX( math.log10( get("X") ) )

def ln ():
    """
    Fonction: log ()
    X = ln(X)
    """
    _setX( math.log( get("X") ) )

def sin ():
    """
    Fonction: sin ()
    X = sin(X)
    """
    _setX( math.sin( get("X") ) )

def cos ():
    """
    Fonction: cos ()
    X = cos(X)
    """
    _setX( math.cos( get("X") ) )

def tan ():
    """
    Fonction: sin ()
    X = sin(X)
    """
    _setX( math.tan( get("X") )  )

def arcsin ():
    """
    Fonction: arcsin ()
    X = arcsin(X)
    """
    _setX( math.sinh( get("X") ) )

def arccos ():
    """
    Fonction: arccos ()
    X = arccos(X)
    """
    _setX( math.cosh( get("X") ) )

def arctan ():
    """
    Fonction: arcsin ()
    X = arcsin(X)
    """
    _setX( math.tanh( get("X") )  )

def toHex ():
    """
    Fonction: toHex ()
    X = sin(X)
    """
    _setX( hex( int( get("X") ) )  )

def toBin ():
    """
    Fonction: toHex ()
    X = sin(X)
    """
    _setX( bin( int( get("X") ) ) )

def toDec ():
    """
    Fonction: toHex ()
    X = sin(X)
    """
    _setX( get("X")  )


def hack ():
    global _pile
    _pile["T"] = "U hav been pwned"
    _pile["Z"] = "Take care of you'r"
    _pile["Y"] = "network and PC"
    _pile["X"] = "Frankline here!"


""" ------ Algoritme de presentation ------ """
if __name__ == "__main__":
    # Affichage doc du fichier
    print(doc)
