#Header 
"""
quoi : différentes fonctions du projet pendu
qui : Baptiste Boiteux
quand : 27-11-2020
"""
#Importation des bibilothèques

import random as r

def choix_mot() :
    """
    La fonction découpe le fichier mots.txt et choisi un mot au hasard
    sortie : mot(str)
    """
    fichier = open("mots.txt",'r')
    for ligne in fichier : 
        liste_mots = ligne.split(',') #Séprartion des mots par par les virgule et ajout dnas la liste liste_mot
    fichier.close()
    mot = r.choice(liste_mots) #choix d'un mot au hasard dans la liste
    return mot
