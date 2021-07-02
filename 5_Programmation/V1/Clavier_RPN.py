# Parametres d'execution
from CONSTANTES import *

doc="""
Fichier: Clavier_RPN.py
Projet: Calculatrice Polonaise Inversse V0.5
Verssion & Date: V1 28.08.2020

Dependances:
- Clavier.py
- RPN.py

Description:
Gestion d'un clavier par matrice
Interface endemique au projet de calculatrice RPN (peut etre adapte facilement a autre matrice de boutons)
La methode exec lire le buffer du clavier (du module Clvaier.py) et executera les fonctions dediees (voir
bas du fichier dans la base de donnees)
On attend que le clavier soit initialiser de l'exterieur


Contenu:


Auteur·e:
- Sleny Martinez (MAS)
- XXX XXX
"""


""" ------ Imports ------ """
# Gestion des exceptions etendue en cas de debug
import micropython
if DEBUG_MODE_CLAVIER: micropython.alloc_emergency_exception_buf(128)

# Imports bibliotheques interne
import machine
import time


# Imports bibliotheques externe officielle (lib)
# Imports bibliotheques externe maisons
import RPN as R
import Clavier
import LCD_RPN


""" ------ Code Utile ------ """
" --- Initialisation --- "
_2nd = False

# --- Initialisation Clavier
# Prototype personnel
#pins_col_N = micropython.const( [17, 21, 14, 15, 16] )
#pins_row_N = micropython.const( [35, 18, 19, 34, 22, 23, 25] )
# Verssion finale
pins_col_N = micropython.const( [12, 13, 14, 15, 16] )
pins_row_N = micropython.const( [17, 18, 19, 21, 22, 23, 25] )
Clavier.init(pins_col_N, pins_row_N)


" --- Systeme --- "
def exec ():
    """
    Fonction: exec()
    Pour chaque touche pressee (trouvee dans le buffer du clavier), realise les opperations
    tel que defini dans la "Base de donnees"
    """
    # Recuperation valleur du 2dn et des fonctions a executer
    global _2nd, _actionTouche, _actionTouche2nd

    # Definition du nombre d'actions
    # Ralisation des opperations
    for touche in Clavier.readBuffer():
        # Pas de 2nd
        if not _2nd:
            # On va chercher la fonction a la ligne / colonne de la touche
            _actionTouche[touche[0]][touche[1]]()
            if DEBUG_MODE_CLAVIER: print(_actionTouche[touche[0]][touche[1]])
        else:
            # On fait la fonction et on desactive le 2nd
            _actionTouche2nd[touche[0]][touche[1]]()
            _2nd = False
            if DEBUG_MODE_CLAVIER: print(_actionTouche2nd[touche[0]][touche[1]])

def _2ndAct ():
    """
    Fonction: _2ndAct()
    Focntion pour la base de donnees pour mettre 2nd a True ou False
    (s'echange a chaque pression de la touche 2nd)
    """
    global _2nd
    _2nd = False if _2nd else True
    # print("2nd : " + str(_2nd))

def _pass ():
    """
    Fonction: _pass()
    Ne fait rien
    """
    pass

def get2nd ():
    """
    Fonction: get2nd()
    Renvoie la valleur de 2nd (bool)
    """
    global _2nd
    return _2nd

def haveToAct ():
    """
    Fonction: haveToAct()
    Renvoie True si des touches sont en attentes, sinon False
    """
    return True if Clavier.any() != 0 else False

def hack ():
    """while True:
        R._pile["T"] = ". . . . . . . . . "
        R._pile["Z"] = " . . .Pipoune. . ."
        R._pile["Y"] = ". . . . . . . . . "
        R._pile["X"] = " . . . . . . . . ."
        LCD_RPN.showRPN()
        time.sleep_ms(500)
        R._pile["T"] = " . . . . . . . . ."
        R._pile["Z"] = ". . . Pipoune . . "
        R._pile["Y"] = " . . . . . . . . ."
        R._pile["X"] = ". . . . . . . . . "
        LCD_RPN.showRPN()
        time.sleep_ms(500)"""

    R._pile["T"] = CREDIT_TEXT[0]
    R._pile["Z"] = CREDIT_TEXT[1]
    R._pile["Y"] = CREDIT_TEXT[2]
    R._pile["X"] = CREDIT_TEXT[3]


""" ------ Base de donnees ------ """
# Fonctionnement des touches
# Chaque touche va appeler une fonction / methode
# La touche 2nd va faire passer la methode de la table _actionTouche a la table _actionTouche2nd
_actionTouche = micropython.const(
[[ _2ndAct , lambda: R.writeX("0b") , lambda: R.writeX("0x") , _pass , R.clear ] ,
[ R.sin , R.cos , R.tan , R.ten_pow_x , R.e_pow_x ] ,
[ lambda: R.writeX("e") , R.pi , R.square , R.power_to, R.divide ] ,
[ _pass , lambda: R.writeX("7") , lambda: R.writeX("8") , lambda: R.writeX("9") , R.multiply ] ,
[ R.rotateDown , lambda: R.writeX("4") , lambda: R.writeX("5") , lambda: R.writeX("6") , R.subtract ] ,
[ R.swapXY , lambda: R.writeX("1") , lambda: R.writeX("2") , lambda: R.writeX("3") , R.add ] ,
[ R.delX , lambda: R.writeX("0") , lambda: R.writeX(".") , R.opposite , R.shiftUp ]])

_actionTouche2nd = micropython.const(
[[ _2ndAct , R.toBin , R.toHex , R.toDec , hack ] ,
[ R.arcsin , R.arccos , R.arctan, R.log , R.ln ] ,
[ lambda: R.writeX("e-") , R.e , R.square_root , R.root , R.modulo ] ,
[ _pass , lambda:R.writeX("A") , lambda:R.writeX("B") , lambda:R.writeX("C") , R.factorial] ,
[ R.rotateUp , lambda:R.writeX("D") , lambda:R.writeX("E") , lambda:R.writeX("F") , R.round ] ,
[ R.lastX , _pass , _pass , _pass , R.sigma ] ,
[ lambda: R.setX(0) , _pass , _pass , R.invert , _pass ]])


""" ------ Algoritme de presentation ------ """
if __name__ == "__main__":
    # Affichage doc du fichier
    print(doc)
