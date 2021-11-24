#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Fait les imports nécéssaires
import time
#Affiche le plateau
print("Les Numéros des cases sont")
print("__________________________________________________________________")
print("!          !          !          !          !          !         !")
print("!    12    !    11    !    10    !     9    !     8    !     7   !")
print("!__________!__________!__________!__________!__________!_________!")
print("!          !          !          !          !          !         !")
print("!     1    !     2    !     3    !     4    !     5    !     6   !")
print("!__________!__________!__________!__________!__________!_________!")

#Définit les listes du jeu
Graine=[4,4,4,4,4,4,4,4,4,4,4,4]
Score=[0,0]
CaseJouables=[1,2,3,4,5,6]
#Affiche le plateau avec le nombre de graines
print("Joueur: 1")
print("__________________________________________________________________")
print("!          !          !          !          !          !         !")
print("   "+str(Graine[11])+"          "+str(Graine[10])+"          "+str(Graine[9])+"          "+str(Graine[8])+"          "+str(Graine[7])+"          "+str(Graine[6])+"    ")
print("!__________!__________!__________!__________!__________!_________!")
print("!          !          !          !          !          !         !")
print("   "+str(Graine[0])+"          "+str(Graine[1])+"          "+str(Graine[2])+"          "+str(Graine[3])+"          "+str(Graine[4])+"          "+str(Graine[5])+"    ")
print("!__________!__________!__________!__________!__________!_________!")
#Définit les différentes variables nécéssaires
ChoixJoueur = 0
CaseEnd = 0
NBRdeG = 0
player = 1
a = 0
c = 0
b = 0
aff = 0
FaminePot=0
NG = 48
clear = "\n" *30
#Boucle Principale
while NG>=3 and Score[0]<25 and Score[0]<25:
    #permet le changement de joueurs en définissant automatiquement player=1
    for player in range(1,3):
        #Redefinission de variables pour pouvoir repartir sur le tour d'après
        f = 0
        ChoixJoueur = 0
        #force le joueur à jouer une case possible
        while ChoixJoueur>6+(player-1)*6 or ChoixJoueur<1+(player-1)*6 or Graine[ChoixJoueur-1]==0 or ChoixJoueur not in CaseJouables:
            if aff == 1:
                print("Case(s) obligatoire(s): "+str(CaseJouables))
            ChoixJoueur = int(input("Nombre de "+str(1+(player-1)*6)+" à "+str(6+(player-1)*6)+": \n"))
        CaseJouables=[1+(player*6)-(player-1)*12,2+(player*6)-(player-1)*12,3+(player*6)-(player-1)*12,4+(player*6)-(player-1)*12,5+(player*6)-(player-1)*12,6+(player*6)-(player-1)*12]
        aff = 0
        #Aligne la valeur choisie avec le fonctionnement d'une liste
        ChoixJoueur = ChoixJoueur - 1
        #Stoque les valeurs utiles dans des variables plusieurs fois pour pouvoir les utiliser à différents endroits
        c = ChoixJoueur
        b = Graine[ChoixJoueur]
        NBRdeG = b
        CaseEnd = c
        #définit la dernière case semée
        while NBRdeG>0:
            NBRdeG = NBRdeG - 1
            CaseEnd = CaseEnd + 1
            if CaseEnd == c:
                CaseEnd = CaseEnd + 1
            if CaseEnd == 12:
                CaseEnd = 0
        #enlève les graines de la case jouée
        Graine[ChoixJoueur] = 0
        #s'occupe du déplacement des graines
        for i in range(1,b+1):
        #évite qu'une graine ne sois semée d'où l'ont est parti
            if ChoixJoueur + i == c:
               ChoixJoueur = ChoixJoueur + 1
            #Permet de retourner au début de la liste quand on atteint la fin
            if ChoixJoueur + i >= 12:
                b = i
                ChoixJoueur = -i
            #ajoute des graines sur la case suivante
            Graine[ChoixJoueur+i]=Graine[ChoixJoueur+i]+1
        #mécanisme qui teste si toutes les graines de l'adversaire vont être mangées
        #Donne la plus grande valeur de l'intervalle d'en face
        a = ((player*6)-(player-1)*12)+5
        #tant que les cases du haut de l'intervalle sont vides verifier celle d'en dessous
        while Graine[a]==0:
            a = a - 1
        #la première case non vide en partant de la borne inférieur de l'intervalle est stockée
        FaminePot = a
        while Graine[a]!=0 and Graine[a]<=2:
            a = a - 1
            #si a a atteint la borne inférieur de l'intervalle et que la case choisi famine
            if (a<((player*6)-(player-1)*12)+6) and CaseEnd==FaminePot:
                f = 1
        while Graine[CaseEnd]<=3 and Graine[CaseEnd]>1 and CaseEnd>=(player*6)-(player-1)*12 and CaseEnd<=((player*6)-(player-1)*12)+5:
            #si il n'y a pas de risques de famine
            if f != 1:
                #les conséquences de la prise de score s'activent
                Score[player-1] = Score[player-1] + Graine[CaseEnd]
                NG = NG - Graine[CaseEnd]
                Graine[CaseEnd] = 0
            CaseEnd = CaseEnd - 1
        #Affichage du plateau et alinéa
        print(clear)
        print("Joueur: "+str(-player+3))
        print("__________________________________________________________________")
        print("!        12!        11!        10!         9!         8!        7!")
        print("   "+str(Graine[11])+"          "+str(Graine[10])+"          "+str(Graine[9])+"          "+str(Graine[8])+"          "+str(Graine[7])+"          "+str(Graine[6])+"    ")
        print("!__________!__________!__________!__________!__________!_________!")
        print("!         1!         2!         3!         4!         5!        6!")
        print("   "+str(Graine[0])+"          "+str(Graine[1])+"          "+str(Graine[2])+"          "+str(Graine[3])+"          "+str(Graine[4])+"          "+str(Graine[5])+"    ")
        print("!__________!__________!__________!__________!__________!_________!")
        print("Scores: Joueur1:  "+str(Score[0]))
        print("        Joueur2:  "+str(Score[1]))
        #Permet de définir si l'adversaire va devoir nourrir le joueur qui vient d finir son tour
        #regarde si toutes les graines du joueur sont vides
        f = 0
        #Définit en fonction du joueur la borne supérieur du plateau de jeu de ce joueur (5 ou 11)
        a = 5+(player-1)*6
        #Descend jusqu'a la borne inférieur du joueur qui vient de jouer
        while Graine[a]==0:
            a = a - 1
            #Si on arrive à cette borne alors on dois forcer l'adversaire à jouer des cases
            if a == (player-1)*6:
                f = 1
        a = 0
        if f == 1:
            #Vide les cases jouables
            CaseJouables=[]
            #Stoque l'information que certaines cases seront obligatoires à jouer
            aff = 1
            #Cherche une par une les cases qui pourrons nourrrir le joueur sans graines
            for i in range(0,6):
                if Graine[((player*6)-(player-1)*12)+5-i] >= i+1:
                    #concatène à la liste ces cases qui seront oblligatoires
                    CaseJouables.append(((player*6)-(player-1)*12)+6-i)
        #Si aucune case ne peut nourrir l'adversaire c'est une fin de partie
        #le joueur qui possède encore des Graines les ajoutes a son score
        if len(CaseJouables)==0 and player==1:
            Score[1]=Score[1]+NG
            #Condition pour break le while principal
            NG==0
        elif len(CaseJouables)==0 and player==2:
            Score[0]=Score[0]+NG
            #Condition pour break le while principal
            NG=0
#Mécanisme de fin de partie qui intervient à la fin de la boucle principale
print("Fin de parti")
Score[0]=Score[0]+(NG//2)
Score[1]=Score[1]+(NG//2)
if Score[0]>Score[1]:
    print("Victoire du joueur 1")
else:
    print("Victoire du joueur 2")
print("Scores: Joueur1:  "+str(Score[0]))
print("        Joueur2:  "+str(Score[1]))
time.sleep(10)