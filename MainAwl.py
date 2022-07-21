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
liste = [4,4,4,4,4,4,4,4,4,4,4,4]
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

        #Initialisation de la saisie protégée
        choix=-1

        #Fin de partie par famine inévitable
        if tour.casjfam()!=[]:

            #Mecanisme de saisie protege
            while (choix not in tour.joueur()) or (choix not in tour.casjfam()) or (liste[choix-1]==0) or (not isinstance(choix,int)):
                choix=input("Choix du joueur"+str(player)+ "\n")
                #Permet d'éviter que le code saute tout en convertissant si possible
                try:
                    choix=int(choix)
                except:
                    pass
            #Creation d'un objet pour jouer le tour
            coup=Ccoup(choix,player,liste,score1,score2,tour)
        
            #appel de la méthode déplacement pour mettre à jour la liste
            coup.deplacement()
            #appels pour mettre à jour les scores et le plateau
            liste,score1,score2=coup.recuperation()

            #Activation des classes pour l'affichage
            aff=Cplateau(liste,score1,score2)
            aff.affichagep()
            aff.affichages()
        else:
            grainesrestantes=sum(liste)
            #On donne le reste au joueur
            if player==1:
                score1+=grainesrestantes
            else:
                score2+=grainesrestantes
            #On vide le plateau
            liste=[0,0,0,0,0,0,0,0,0,0,0,0]
            #On affiche
            print("\033[32mFin par famine inévitable\nLe Joueur "+str(player)+" ne peut plus nourrir l'adversaire\nLe joueur "+str(player)+" récupère le reste des graînes\033[37m")
            aff=Cplateau(liste,score1,score2)
            aff.affichagep()
            aff.affichages()
            break

#Conditions de fin de partie
print("_______Fin de partie_______")
if score1>score2:
    print("victoire du joueur 1")
else:
    print("Victoire du joueur 2")
            
