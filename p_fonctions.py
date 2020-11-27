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

def affichage_mot(mot,i_lettre):
    """
    affiche la lettre d'indice i_lettre de mot et des _ pour les lettres restantes
    entrée : mot(str), lettre(int)
    """
    aff = ""
    for i in range(len(mot)):
        if (i == i_lettre):
            aff += ' ' + mot[i_lettre]
        else:
            aff += ' _'
    print(aff)

def detection_lettre(mot):
    lettre = input()
    if (lettre in mot) == True :
        print("gagné")



    
