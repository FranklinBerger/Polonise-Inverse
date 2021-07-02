doc="""
Fichier: CONSTANTES.py
Projet: Calculatrice Polonaise Inversse V0.5
Verssion & Date: V1 24.09.2020

Dependances:

Description:
Gestion des constantes d'execution de la calculatrice, principalement des
modes debug
N'impacte pas les modules non-endemique qu projet (voir dirrectement le code
dansce cas)

Contenu:


Auteur·e:
- Sleny Martinez (MAS)
- XXX XXX
"""
# micropytjon.const => initialisation de constantes
import micropython

""" --- Constantes --- """
# Affiche les erreurs generale du projet
DEBUG_MODE_MAIN = micropython.const(True)
# Affiche les activites du clavier
DEBUG_MODE_CLAVIER = micropython.const(True)
# Affiche les activites de l'ecrant
DEBUG_MODE_LCD = micropython.const(True)
# Texte affiche pour l'allumage
START_TEXT = [
"Calculatrice RPN",
"ETML 2020-2021",
"Frankline Berger"]

# Texte de credits si 2nd + Clear
CREDIT_TEXT = [
"Calculatrice RPN",
"ETML 2020-2021",
"V1.0 Avril 2021",
"@FranklinBerger"]
