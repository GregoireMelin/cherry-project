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
def Repondre(reponse):
    pygame.mixer.init()
    tts=gTTS(reponse,lang='fr')
    tts.save("temp.mp3")
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
            continue

############# PROGRAMME ###################################################
Requeteutilisateur=ReconnaissanceVocaleGoogle()
if Requeteutilisateur=="Bonjour":
    Repondre('Bonjour, Aimes tu le football ?')
    Requeteutilisateur=ReconnaissanceVocaleGoogle()
    print(Requeteutilisateur)
    if Requeteutilisateur=="oui":
        Repondre('Je peux te dire les deux derniers matchs de ligue 1 qui ont eu lieu, les veux tu ?')
        Requeteutilisateur=ReconnaissanceVocaleGoogle()
        print(Requeteutilisateur)
        if Requeteutilisateur=="oui":
            match=getDernierMatchs()
            Repondre('Les 2 derniers matchs qui ont eu lieu sont '+match[0]+' et '+match[1])
        else:
            Repondre('Ce nest pas un drame parlons dautre chose')
    else:
        Repondre('Ce nest pas un drame parlons dautre chose')
else:
    tts=gTTS("La réponse est 42.",lang='fr')
