#!/usr/bin/env python
# -*- coding: utf-8 -*-
############# BIBLIOTHEQUES ##############################################
import urllib
import sys
import os
from feedparser import parse
from gtts import gTTS
import pygame
import speech_recognition as sr
############# METHODES ###################################################
###Fonction qui recupere les 2 derniers matchs de ligue 1
def getDernierMatchs():
    lien="http://www.matchendirect.fr/rss/foot-ligue-1-c16.xml"
    contenu=parse(lien)
    matchs=[]
    for element in contenu.entries:
        if not element.title[len(element.title)-9:]=="en direct":
           matchs.append(element.title[10:])
    return(matchs)

###Fonction de reconnaissance vocale utilisant l'API Google
def ReconnaissanceVocaleGoogle():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dites quelques chose")
        audio = r.listen(source)
    try:
        return(r.recognize_google(audio,language='fr'))
    except sr.UnknownValueError:
        print("Je n'ai pas compris")
    except sr.RequestError as e:
        print("Le serveur a invalide votre requete; {0}".format(e))

###Fonction qui permet au programme de repondre en utilisant l'API Google
def Repondre():
        matchs=getDernierMatchs()
        pygame.mixer.init()
        tts=gTTS('Les 2 derniers matchs qui ont eu lieu sont '+matchs[0]+' et '+matchs[1],lang='fr')
        tts.save("temp.mp3")
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

############# PROGRAMME ###################################################
Requeteutilisateur=ReconnaissanceVocaleGoogle()
print(Requeteutilisateur)
if Requeteutilisateur=="match":
    Repondre()
else:
    tts=gTTS("Je l'ignore mais tu peux chercher sur Google",lang='fr')
os.remove('temp.mp3')
