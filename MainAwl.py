#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 09:07:01 2021

@author: jc.burnot
Ce programme est le programme principal de l'awalé
C'est celui qui est exécuté pour que l'on puisse jouer
"""

#gere les importation necessaires
from CJouable import Cjouable
from CPlateau import Cplateau
from CCoup import Ccoup

#definit l'historique
#historique=[]

#Definit la liste de départ
#liste = [4,4,4,4,4,4,4,4,4,4,4,4]
liste = [4,4,4,4,4,4,1,2,0,0,0,0]
#definit les scores de depart
score1=0
score2=0

#initialise le premier tour
player=1
init=Cplateau(liste,score1,score2)
init.affichagep()
init.affichages()

#correspond à la Condition de sortie du jeu
while score1<25 and score2<25:
    
    #permet le changement de joueurs
    player=1 
    for player in range(1,2+1):
        
        #Creer l'objet pour la saisie protégée
        tour=Cjouable(player,liste)
        
        #Mecanisme de saisie protege
        choix=-1
        while choix not in tour.joueur() and choix not in tour.casjfam():
            choix=int(input("Choix du joueur"+str(player)+ "\n"))
            
        #Creation d'un objet pour jouer le tour
        coup=Ccoup(choix,player,liste,score1,score2)
        
        #appel de la méthode déplacement pour mettre à jour la liste
        coup.deplacement()
        #appels pour mettre à jour les scores et le plateau
        liste,score1,score2=coup.recuperation()

        #Activation des classes pour l'affichage
        aff=Cplateau(liste,score1,score2)
        aff.affichagep()
        aff.affichages()
        
#Conditions de fin de partie
print("_______Fin de partie_______")
if score1>score2:
    print("victoire du joueur 1")
else:
    print("Victoire du joueur 2")
            
