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
_threadRun = True
_delayFrame = 0
_delayStep = 0

def init (col, row, delayFrame = 1, delayStep = 5):
    """
    Fonction: init (col, row, delayFrame = 50, delayStep = 5)
    Initialisation du clavier
    col & row: liste contenant les N° GPIOs de chaque pin (dans l'ordre)
    """
    global _col, _row, _mem, _threadRun, _delayFrame, _delayStep
    _delayFrame = delayFrame
    _delayStep = delayStep
    
    # Initialisation lignes
    index = 0
    row_mem = []
    for r in row:
        _row.append([ index, machine.Pin(r,mode=machine.Pin.IN,pull=machine.Pin.PULL_DOWN) ])
        row_mem.append(index + 1)
        index += 1
    # Initialisation colonnes
    index = 0
    for c in col:
        # value = 1 : colonne desactivee
        _col.append([ index, machine.Pin(c,mode=machine.Pin.OPEN_DRAIN,value=1) ])
        _mem.append(row_mem)
        index += 1
    
    # Initialisation anti-doublon
    #r = [1] * len(_row)
    #_row_mem = [r] * len(_col)
    _mem = [[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[2,2,2,2,2,2,2],[3,3,3,3,3,3,3],[4,4,4,4,4,4,4]]
    



" --- Systeme --- "
def threadClavier (arg=None):
    """
    Fonction: threadClavier (arg=None)
    Thread de lecture en continu du clavier
    """
    global _col, _row, _mem, _threadRun, _delayFrame, _delayStep, _bufferKey
    
    
    # Jusqu'a ce qu'on arete le thread
    while _threadRun:
        # Balayage Colonne
        for c in _col:
            # Activation colonne et stabilisation HW
            c[1].value(0)
            time.sleep_ms(_delayStep)
            # Lecture lignes
            print("C: " + str(c[0]) + " : " + str(_mem[c[0]]))
            for r in _row:
                #print("r: " + str(r) + " C: " + str(c) + " => " + str(_row_mem[c[0]][r[0]]))
                r_val = r[1].value()
                r_Oval = _mem[c[0]][r[0]]
                if r[0]==0 and c[0]==4 and DEBUG_MODE:
                    print("...")
                    print(r_val)
                    print(r_Oval)
                # Test flanc montant par XOR
                if r_val == True and r_val ^ r_Oval:
                    # Enregistrement pression dans buffer
                    _bufferKey.append([ r[0] , c[0] ])
                # Enregistrement valleur pour suite (anti-doublon)
                _mem[c[0]][r[0]] = r_val
            # Desactivation colonne
            c[1].value(1)
        # Fin frame, delais
        time.sleep_ms(_delayFrame)
    
    



""" ------ Algoritme de presentation ------ """
if __name__ == "__main__":
    # Affichage doc du fichier
    print(doc)


