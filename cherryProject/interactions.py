### Bibliotheque
from gtts import gTTS
import pygame
import os
import speech_recognition as sr
import subprocess
import urllib
import sys
import os
from feedparser import parse
import random

###Fonction qui permet au programme de repondre en utilisant l'API Google
def debutTransmission():
        pygame.mixer.init()
        pygame.mixer.music.load("../bin/up.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

def finTransmission():
        pygame.mixer.init()
        pygame.mixer.music.load("../bin/down.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

def Repondre(reponse):
        pygame.mixer.init()
        tts=gTTS(reponse,lang='fr')
        tts.save("temp.mp3")
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        os.remove("temp.mp3")

def RepondreESpeak(texte,nomFichier):
   subprocess.call(["espeak",texte,"-vfr","-w "+nomFichier+".wav"])

def RepondreESpeakStreaming(texte):
   subprocess.call(["espeak",texte,"-vfr"])
###Fonction de reconnaissance vocale utilisant l'API Google
def ReconnaissanceVocaleGoogle():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Dites quelques chose")
        audio = r.listen(source)
    try:
        return(r.recognize_google(audio,language='fr'))
    except sr.UnknownValueError:
        print("Cherry reflechit attend le signal sonore avant de parler")
    except sr.RequestError as e:
        print("Le serveur a invalide votre requete; {0}".format(e))

def CreationBaseDeConversation(fichierDialogue):
	fichier=open(fichierDialogue,'r')
	lignes=fichier.readlines()
	conversation=['Jaime les pizzas','Moi aussi']
	#ENTRAINEMENT DU CHATBOT
	i=0
	for ligne in lignes:
		conversation.append(ligne[0:-1])
	return(conversation)

def getVDM():
    lien="https://www.viedemerde.fr/rss"
    contenu=parse(lien)
    matchs=[]
    for element in contenu.entries:
        if not element.title[len(element.title)-9:]=="en direct":
           matchs.append(element.summary[3:len(element.summary)-7])
    return(matchs)
