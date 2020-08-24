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

# Imports bibliotheques externe officielle (lib)


# Imports bibliotheques externe maisons
import Clavier
import RPN
import PCF8574
import LCD_2004




""" ------ Code Utile ------ """
" --- Initialisation --- "
# --- Initialisation Clavier
pins_col_N = micropython.const( [12, 13, 14, 15, 16] )
pins_row_N = micropython.const( [17, 18, 19, 21, 22, 23, 25] )

Clavier.init(pins_col_N, pins_row_N)








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


" --- Systeme --- "



