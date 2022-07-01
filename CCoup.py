#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:23:55 2021

@author: jc.burnot
Ce programme est une classe qui gère les coups jouées et les scores
"""
from CJouable import Cjouable
class Ccoup:
    def __init__(self,choix,player,liste,score1=0,score2=0):
        self.__choix=choix
        self.__liste=liste
        self.__player=player
        self.__score1=score1
        self.__score2=score2
        
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
        choix1=self.__choix-1
        #rajoute des graine dans le cas ou il y a un tour complet
        self.__liste[choix1] = self.__liste[choix1]+self.nbtc()
        for i in range(1,self.__liste[choix1]+1):
            choix1=(choix1+1)%12
            self.__liste[choix1]+=1
        self.__liste[self.__choix-1]=0
        #choix1 correspond à l'indice de la dernière case semée (comptage joueur)
        return self.__liste,choix1+1
    
    #defini si la dernière case est semée chez l'adversaire
    def caseadv(self):
        #creer un objet de la classe Cjouable
        jouable1=Cjouable(self.__player,self.__liste)
        
        #print(self.deplacement()[1])
        
        if self.deplacement()[1] in jouable1.adversaire():
            return True
        else:
            return False
    
    #defini si une case est mangeable après la distribution
    def mangeable(self):
        if self.caseadv()==False:
            return False
        else:
            if self.__liste[self.__choix-1]==3 or self.__liste[self.__choix-1]==4:
                return True
            else:
                return False
        
    #Vérifie que le coup ne provoque pas la famine si il y a famine on active une variable
    def Comfam(self):
        #creer un objet de la classe Cjouable
        jouable2=Cjouable(self.__player,self.__liste)
        if self.__choix-1 != jouable2.bornsup():
            for i in range((self.__choix-1)+1,jouable2.bornsup()+1):
                if self.__liste[i]!=0:
                    return False
                else:
                    for i in range((self.__choix-1),jouable2.borninf()-1,-1):
                        if self.mangeable(self.__liste,i)==False:
                            return False
                        else:
                            return True
            
        else:
            for i in range((self.__choix-1),jouable2.borninf()-1,-1):
                        if self.mangeable(self.__liste,i)==False:
                            return False
                        else:
                            return True     
    
    #gere la récuperation des graines et meca et compte combien on été récupérées
    def recuperation(self):
        #print("On m'appelle pour que je mange")
        #creer un objet de la classe Cjouable
        jouable3=Cjouable(self.__player,self.__liste)
        if self.Comfam()==True:
            print("Non, si on prend c'est la famine") 
            return self.__liste,self.__score1,self.__score2
        else:
            i=self.__choix-1
            while self.mangeable()==True and i >= jouable3.borninf():
                print("Miam")
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
                
                
        

