#Header 
"""
quoi :Programme principal projet pendu
qui : Baptiste Boiteux
quand : 27-11-2020
"""

#Importation des bibilothèques
import p_fonctions as p


start = 1
restart = ""
score = [0]
while start == 1 :
    mot = p.choix_mot()
    chance = 8
    l_entree = [mot[0]]
    prop = ""
    print(p.detection_lettre(mot,l_entree)+"\n")
    while chance > 0 and mot != prop :
            print("il vous reste "+ str(chance) +" chances\n")
            print("Veuillez entrer une lettre :\n")
            entree = input()
            if entree in l_entree :
                print("!la lettre est déjà rentrée!\n")
            else:
                l_entree.append(entree)
                if not(entree in mot):
                    chance -= 1
            prop = p.detection_lettre(mot,l_entree)
            print(prop+"\n")
    if chance > 0 :
        print("Gagné !\n Il vous restait :"+str(chance)+" chances\n")
        score.append(chance)
        chance = 0
    else :
        print("YOU LOOSE")
    print("Le meileur score est :"+str(max(score)))
    while not(restart in ['o','n']) :
        print("Voulez-vous rejouer ? Taper o pour oui et n pour non")
        restart = input()
        if restart == 'n':
            start = 0
        if restart == 'o':
            start = 1
        else :
            print("!le caractère rentré n'est pas valide!")
        



