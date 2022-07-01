#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 08:12:50 2021

@author: jc.burnot
Ce programme gère le plateau de jeu le choix du joueur et les scores
"""
#from CCoup import Ccoup
class Cplateau:
    def __init__(self,liste,score1,score2):
        self.__liste=liste
        self.__score1=score1
        self.__score2=score2
        
    #Permet de gerer l'affichage du plateau
    def affichagep(self):
        print("En rouge le numéro de case")
        print("En vert le nombre de graines")
        print("\033[37m__________________________________________________________________")
        print("!        \033[31m12\033[37m!        \033[31m11\033[37m!        \033[31m10\033[37m!         \033[31m9\033[37m!         \033[31m8\033[37m!        \033[31m7\033[37m!")
        print("     \033[32m"+str(self.__liste[11])+"\033[37m          \033[32m"+str(self.__liste[10])+"\033[37m          \033[32m"+str(self.__liste[9])+"\033[37m          \033[32m"+str(self.__liste[8])+"\033[37m          \033[32m"+str(self.__liste[7])+"\033[37m          \033[32m"+str(self.__liste[6])+"\033[37m    ")
        print("!__________!__________!__________!__________!__________!_________!")
        print("!         \033[31m1\033[37m!         \033[31m2\033[37m!         \033[31m3\033[37m!         \033[31m4\033[37m!         \033[31m5\033[37m!        \033[31m6\033[37m!")
        print("     \033[32m"+str(self.__liste[0])+"\033[37m          \033[32m"+str(self.__liste[1])+"\033[37m          \033[32m"+str(self.__liste[2])+"\033[37m          \033[32m"+str(self.__liste[3])+"\033[37m          \033[32m"+str(self.__liste[4])+"\033[37m          \033[32m"+str(self.__liste[5])+"\033[37m    ")
        print("!__________!__________!__________!__________!__________!_________!")
                
    #gere l'affichage des scores    
    def affichages(self):
        print("Scores actuels:")   
        print("joueur 1:",self.__score1)
        print("joueur 2:",self.__score2)
        
