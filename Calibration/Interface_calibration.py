# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 12:17:40 2017

@author: henry
"""

from tkinter import *
from tkinter.messagebox import *
import Calcule_homographie

def annule(L,l):
    for i in range (len(L)):
        L.pop()
        l.pop()
    print(l,L)

def calcule(Lx, LX):
    print(Lx, LX)
    H = Calcule_homographie.homography(Lx,LX)
    
    
    fenetre_resultat = Tk() #définition de la fenêtre
    fenetre_resultat.title('Résultat calcul')
    
    labelH=Label(fenetre_resultat, text='H = ' + str(H))
    labelH.pack()
    
    
    
    b1=Button(fenetre_resultat, text='Quitter', command= fenetre_resultat.destroy)
    b1.pack(side = BOTTOM, padx = 3, pady = 3)
    
    fenetre_resultat.mainloop()

def ajoute(Lx, LX):
    X=float(nbReel1.get())
    Y=float(nbReel2.get())
    Z=float(nbReel5.get())
    x=float(nbReel3.get())
    y=float(nbReel4.get())
    Lx.append([x,y])
    LX.append([X,Y,Z,1])
    print(Lx)
    print(LX)
    if len(LX)>=6:
        Calculer.config(state="normal")


#def main():
    
LX = []
Lx = []

fenetre = Tk() #définition de la fenêtre
fenetre.title('Calibration projecteur')

label=Label(fenetre, text="Insérez vos données et lancez le calcul")
label.pack()

b1=Button(fenetre, text='Quitter', command= fenetre.destroy)
b1.pack(side = BOTTOM, padx = 3, pady = 3)

reel1 = Label(fenetre, text= "Coordonnée x dans l'espace de projection : le sol (m)")
reel1.pack()
nbReel1 = Entry(fenetre)
nbReel1.pack()


reel2 = Label(fenetre, text= "Coordonnée y dans l'espace de projection : le sol (m)")
reel2.pack()
nbReel2 = Entry(fenetre)
nbReel2.pack()

reel5 = Label(fenetre, text= "Coordonnée z dans l'espace de projection : le sol (m)")
reel5.pack()
nbReel5 = Entry(fenetre)
nbReel5.pack()

reel3 = Label(fenetre, text= "Coordonnée x dans l'espace de projeté : l'écran (pixels)")
reel3.pack()
nbReel3 = Entry(fenetre)
nbReel3.pack()

reel4 = Label(fenetre, text= "Coordonnée y dans l'espace de projection : l'écran (pixels)")
reel4.pack()
nbReel4 = Entry(fenetre)
nbReel4.pack()

Ajouter=Button(fenetre, text="Ajouter", command= lambda : ajoute(Lx, LX))
Ajouter.pack()

Calculer=Button(fenetre, text="Calculer", command= lambda : calcule(Lx, LX))
Calculer.pack()
Calculer.config(state=DISABLED)

Annuler=Button(fenetre, text="Annuler", command=lambda : annule(Lx,LX))
Annuler.pack()

fenetre.mainloop()

#main()