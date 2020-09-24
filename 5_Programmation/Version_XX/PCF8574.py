# CONSTANTES & PARAMETRES
import micropython
DEBUG_MODE = micropython.const(False)
# Prototype personnel
PCF8574_ADDRESS = micropython.const(32)
# Verssion finale
#PCF8574_ADDRESS = micropython.const(56)

doc="""
Fichier: PCF8574.py
Projet: Calculatrice Polonaise Inversse V0.5
Verssion & Date: V1 15.08.2020

Dependances:

Description:
Ecriture et lecture au travers d'un IO extender PCF8574
Contenu sous la forme d'une classe PCF8574
L'I2C est contenu sous forme d'objet introduit a l'instanciation

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

# Imports bibliotheques externe officielle (lib)
# Imports bibliotheques externe maisons




""" ------ Code Utile ------ """
" --- Initialisation --- "

" --- Systeme --- "
class PCF8574 (object):
    def __init__(self, i2cBus, pcfAadress = 0):
        """
        Constructeur: __init__(i2cBus, pcfAadress = 0)
        Instanciaion d'un objet PCF8574
        """
        self.i2cBus = i2cBus
        self.pcfAadress = pcfAadress

    def read (self):
        """
        Methode: read(self)
        Lis la valleur dans l'IO extender, renvoie sous forme de int
        """
        return self.i2cBus.readfrom(PCF8574_ADDRESS + self.pcfAadress, 1)[0]

    def write (self, value):
        """
        Methode: write(self)
        Lis la valleur dans l'IO extender, renvoie sous forme de int
        """
        return self.i2cBus.writeto( PCF8574_ADDRESS + self.pcfAadress , value.to_bytes(1, "big") )




""" ------ Algoritme de presentation ------ """
if __name__ == "__main__":
    # Affichage doc du fichier
    print(doc)
