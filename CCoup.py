#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:23:55 2021

@author: jc.burnot
Ce programme est une classe qui gère les coups jouées et les scores
"""
from CJouable import Cjouable
class Ccoup:
    def __init__(self,choix,player,liste,score1,score2,arrive=-1):
        self.__choix=choix
        self.__liste=liste
        self.__player=player
        self.__score1=score1
        self.__score2=score2
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
        #Permet de regler le déphasage des indices
        self.__arrive+=1
    
    #defini si une case est mangeable après la distribution
    def mangeable(self,trou):
        jouable1=Cjouable(self.__player,self.__liste)
        if trou not in jouable1.adversaire():
            return False
        else:
            if self.__liste[trou-1]==2 or self.__liste[trou-1]==3:
                return True
            else:
                return False
        
    #Vérifie que le coup ne provoque pas la famine si il y a famine on active une variable
    """
    Fonction complètement à refaire.
    """
    def Comfam(self):
        #creer un objet de la classe Cjouable
        jouable2=Cjouable(self.__player,self.__liste)

        if self.__arrive-1 != jouable2.bornsup():
            #print("t'es pas arrivé sur la borne sup de l'adversaire",jouable2.bornsup())
            for i in range((self.__arrive-1)+1,jouable2.bornsup()+1):
                if self.__liste[i]!=0:
                    #print("Une des cases plus haute que l'endroit que t'as touché n'est pas nulle il n'y aura jamais de famine")
                    return False
                else:
                    for i in range((self.__choix-1),jouable2.borninf()-1,-1):
                        if self.mangeable(i)==False:
                            return False
                        else:
                            return True
        else:
            #print("t'es arrivé sur la borne sup de l'adversaire!",jouable2.bornsup())
            for i in range((self.__choix-1),jouable2.borninf()-1,-1):
                        if self.mangeable(i)==False:
                            return False
                        else:
                            return True     
    
    #gere la récuperation des graines et meca et compte combien on été récupérées
    def recuperation(self):
        #creer un objet de la classe Cjouable
        jouable3=Cjouable(self.__player,self.__liste)
        if self.Comfam()==True:
            return self.__liste,self.__score1,self.__score2
        else:
            i=self.__choix-1
            #print("Miam", self.mangeable(), jouable3.borninf())
            while self.mangeable(self.__arrive)==True and i >= jouable3.borninf():
                #Cas du joueur1
                if self.__player==1:
                    self.__score1+=self.__liste[i]
                    self.__liste[i]=0
                    i-=1
                #Cas du joueur2
                elif self.__player==2:
                    self.__score2+=self.__liste[i]
                    self.__liste[i]=0
                    i-=1
            return self.__liste,self.__score1,self.__score2
                
                
        

