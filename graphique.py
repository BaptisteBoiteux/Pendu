#Header 
"""
quoi :Programme du projet pendu graphique
qui : Baptiste Boiteux
quand : 11-12-2020
TODO : faire la partie d'affichage des images
"""

#Importation des bibilothèques
import p_fonctions as p
from tkinter import Tk, Label, Button, Canvas, Entry, StringVar,messagebox, PhotoImage,filedialog

mot = p.choix_mot()
l_entree = [mot[0]]
""" ici je met la fonction verfication dans le programme directement car elle gère les elements graphique
vu avec un professeur"""

def Verification():
    """
    Met à jour les varibales d'affichage en détectant si la lettre est dans le mot
    """
    global chance
    global entree
    global prop
    content = chance.get()
    parts = content.split(':')
    vie = int(parts[1])
    if entree.get() in l_entree :
        messagebox.showinfo("Erreur!","la lettre est déjà rentrée")
    else :
        l_entree.append(entree.get())
        if not(entree.get() in mot):
            vie -= 1
            chance.set("chance :"+str(vie))
            messagebox.showinfo("perdu","tu perd une vie")
        else :
            messagebox.showinfo("gagné","la lettre est dans le mot")
    prop.set(p.detection_lettre(mot,l_entree))
    """if vie == 8 :
        Canevas.delete('all') # on efface la zone graphique
        photo = PhotoImage(file = bonhomme8.gif)
        gifdict[bonhomme8.gif] = photo  # référence
        print (gifdict)
        Canevas.create_image(0,0,anchor = 'nw',image = photo)
        Canevas.config(height = photo.height(),width = photo.width())
        mw.title("Image " + str(photo.width()) + " x " + str(photo.height()))"""

# création de la fenêtre graphique
mw = Tk()
chance = StringVar()
chance.set("chance:8")
prop = StringVar()
prop.set(p.detection_lettre(mot,l_entree))
mw.title('Pendu')
# Création d'un widget Canvas (zone graphique)
Largeur = 480
Hauteur = 320
Canevas = Canvas(mw, width = Largeur, height =Hauteur, bg ='grey')
Canevas.pack(side = 'right',padx =5, pady =5)
# Création d'un widget Button (bouton Proposer)
Button(mw, text ='Proposer' ,command = Verification).pack(side='left',padx=5,pady=5)
# Création d'un widget Entry (champ de saisie)
entree = StringVar()
Champ = Entry(mw, textvariable = entree, bg = 'bisque', fg = 'maroon')
Champ.pack(side = 'left', padx = 5, pady = 5)
# Création d'un widget Label (chance)
Label1 = Label(mw, textvariable = chance)
Label1.pack(side = 'bottom', padx = 5, pady = 5)
# Création d'un widget Label (mot)
Label1 = Label(mw, textvariable = prop)
Label1.pack(side = 'right', padx = 5, pady = 5)
# Utilisation d'un dictionnaire pour conserver une référence
gifdict = {}
#lancement du gestionnaire d'événements
mw.mainloop()


            