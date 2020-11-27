def decoupage_mots :
    fichier = open("mots.txt")
    liste_mots = []
    for ligne in fichier :
        mot =ligne.split(',')
        liste_mots.append(mot)
    return liste_mots
    
