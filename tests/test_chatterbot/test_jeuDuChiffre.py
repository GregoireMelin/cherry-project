#RANDOM NUMBER GAME
from interactions import ReconnaissanceVocaleGoogle
from interactions import Repondre
import random


compnum = random.randrange(50)
Repondre('Jouons au jeu du chiffre. Je pense a un chiffre entre 0 et 50 mais quel est il')
#cheat mode : print compnum
usenum=ReconnaissanceVocaleGoogle()
print(usenum)
print(str(compnum)) #Pour developpement uniquement
while usenum != "stoppons le jeu":
    if usenum == "Choisis un nouveau nombre":
        compnum = random.randrange(50)
        Repondre('Choix dun nombre. Jai choisis a devine le nombre auquel je pense')

    if usenum == "indice":
        Repondre('Voila un indice. Mon nombre se situe entre '+str(compnum-5)+' et '+str(compnum+5))

#	if usenum > compnum :
#        Repondre('trop grand')

#    if usenum < str(compnum) :
#        Repondre('trop petit')

    if usenum == str(compnum):
        Repondre('Bravo tu gagnes pour cette fois ci : on recommence ?')
        rep=ReconnaissanceVocaleGoogle()
        if rep=="oui":
            usenum ="Choisis un nouveau nombre"
        else:
            Repondre('Daccord cest la fin du jeu dommage on samusait bien')
            usenum="Stopons ce jeu"
    else:
        Repondre('Ce nest pas un nombre mais si tu veux quitter le jeu dit moi Stopons ce jeu')

    usenum = ReconnaissanceVocaleGoogle()

import random

nbr_secret = random.randint(1,100)
