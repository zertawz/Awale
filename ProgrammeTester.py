#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 08:29:00 2021

@author: jc.burnot
Ce programme réalise des tests
"""
from CJouable import Cjouable
from CPlateau import Cplateau
#from CCoup import Ccoup
player=1
liste = [4,4,2,4,6,4,2,4,2,4,8,3]
tour1a=Cjouable(player,liste)
tour1b=Cplateau(liste)
#print(tour1.liste)
#print(tour1.joueur(player))
#print(tour1.adversaire(player))
#print(tour1a.sommeadv(player,liste))
print(tour1b.affichagep(liste))
print(tour1a.semadv(player,liste))
