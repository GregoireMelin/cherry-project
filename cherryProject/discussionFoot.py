#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import sys
import os
from feedparser import parse
from interactions import *
import utilisateur

###Fonction qui recupere les 2 derniers matchs de ligue 1
def getDernierMatchs():
    lien="http://www.matchendirect.fr/rss/foot-ligue-1-c16.xml"
    contenu=parse(lien)
    matchs=[]
    for element in contenu.entries:
        if not element.title[len(element.title)-9:]=="en direct":
           matchs.append(element.title[10:])
    return(matchs)


print("Cherry : ")
Repondre('Aimes tu le football ?')
print("Aimes tu le football ?")
debutTransmission()
Requeteutilisateur=ReconnaissanceVocaleGoogle()
finTransmission()
print("Tu as dit :")
print(Requeteutilisateur)
if not Requeteutilisateur==None:
    if "oui" in Requeteutilisateur:
    	print("Cherry : ")
    	Repondre('Je peux te dire les deux derniers matchs de ligue 1 qui ont eu lieu, les veux tu ?')
    	print("Je peux te dire les deux derniers matchs de ligue 1 qui ont eu lieu, les veux tu ?")
	debutTransmission()
    	Requeteutilisateur=ReconnaissanceVocaleGoogle()
	finTransmission()
    	print("Tu as dit :")
    	print(Requeteutilisateur)

    if "oui" in Requeteutilisateur:
        match=getDernierMatchs()
        print("Cherry : ")
		
        Repondre('Les 2 derniers matchs qui ont eu lieu sont '+match[0]+' et '+match[1])
        print("Les 2 derniers matchs qui ont eu lieu sont "+match[0]+ " et "+match[1])
    else:
        print("Cherry : ")
        Repondre('Comme tu voudras')
        print("Comme tu voudras")
else:
    print("Cherry : ")
    Repondre('Ce nest pas un drame parlons dautre chose')
    print("Ce nest pas un drame parlons dautre chose")
print("Cherry : ")
Repondre('Parlons dautres choses')
print("Parlons dautres choses")
