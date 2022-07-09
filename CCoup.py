#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:23:55 2021

@author: jc.burnot
Ce programme est une classe qui gère les coups jouées et les scores
"""
from CJouable import Cjouable
class Ccoup:
    def __init__(self,choix,player,liste,score1,score2,tour,arrive=-1):
        self.__choix=choix
        self.__liste=liste
        self.__player=player
        self.__score1=score1
        self.__score2=score2
        self.__tour=tour
        self.__arrive=arrive
        
    #Definit le nombre de tours que va faire le choix
    def nbtc(self):
        if self.__liste[self.__choix-1]>=45:
            return 4
        elif self.__liste[self.__choix-1]>=34:
            return 3
        elif self.__liste[self.__choix-1]>=23:
            return 2
        elif self.__liste[self.__choix-1]>=11:
            return 1
        else:
            return 0

    #permet de gérer le déplacement des graines en fonction du coup et de stocker le dernier indice
    def deplacement(self):
        self.__arrive=self.__choix-1
        #rajoute des graine dans le cas ou il y a un tour complet
        self.__liste[self.__arrive] = self.__liste[self.__arrive]+self.nbtc()
        for i in range(1,self.__liste[self.__arrive]+1):
            self.__arrive=(self.__arrive+1)%12
            self.__liste[self.__arrive]+=1
        self.__liste[self.__choix-1]=0
        #Permet de regler le déphasage des indices (on joue entre 1 et 12)
        self.__arrive+=1
        #Mise à jour de l'attribut liste pour l'attribut tour
        self.__tour.liste=self.__liste
    
    #defini si une case est mangeable après la distribution
    def mangeable(self,trou):
        if trou not in self.__tour.adversaire():
            return False
        else:
            if self.__liste[trou-1]==2 or self.__liste[trou-1]==3:
                return True
            else:
                return False
        
    #Vérifie que le coup ne provoque pas la famine si il y a famine on renvoit True
    def Comfam(self):
        if not self.mangeable(self.__arrive):
            return False
        #Cas ou on ne tombe pas sur la bornesup de l'adversaire
        elif self.__arrive-1 != self.__tour.bornsup():
            #Est ce qu'il y a des trou non vide au dessus de l'indice d'arrivé
            for i in range((self.__arrive-1)+1,self.__tour.bornsup()+1):
                if self.__liste[i]!=0:
                    #si il y en a un il n'y aura jamais de famine
                    return False
            """
            Toutes les cases au dessus sont vides. Testons la mangeabilité des trous inf
            -Pas besoin de tester l'indice de l'endroit où on tombe cf:premier if
            -la fonction borninf retourne l'indice en comptage python
            ce qui compense le -1 à mettre pour vérifier le trou avec l'indice
            le plus bas.
            """
            for i in range((self.__arrive-1),self.__tour.borninf(),-1):
                if self.mangeable(i)==False:
                    #Si un des trou inf n'est pas mangeable pas de famine
                    return False
            #Tout est mangeable attention famine!
            return True
        else:
            """
            Cas où on tombe sur la bornesup de l'adversaire:
            On doit tester si toutes les cases de l'adversaire sont mangeables.
            De la borne maximale à la borne minimale.
            """
            for i in range(self.__arrive, self.__tour.borninf(),-1):
                if self.mangeable(i)==False:
                    return False
            #tout est mangeable: de bornesup à borneinf
            return True

    #gere la récuperation des graines et meca et compte combien on été récupérées
    def recuperation(self):
        if self.Comfam()==True:
            return self.__liste,self.__score1,self.__score2
        else:
            i=self.__arrive
            #tant que les cases suivantes sont mangeables on continue
            while self.mangeable(i)==True and i>self.__tour.borninf():
                #Cas du joueur1
                if self.__player==1:
                    self.__score1+=self.__liste[i-1]
                    self.__liste[i-1]=0
                    i-=1
                #Cas du joueur2
                elif self.__player==2:
                    self.__score2+=self.__liste[i-1]
                    self.__liste[i-1]=0
                    i-=1
            return self.__liste,self.__score1,self.__score2
