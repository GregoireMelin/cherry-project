#!/usr/bin/env python3
################### IMPORTATION DES DEPENDANCES ##################################
# -*- coding: utf-8 -*-
import os
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from creerConversation import dialogue
import subprocess
#from donneesSpatioTemporelles import DonneLHeure, DonneLaDate
################### FIN IMPORTATION DES DEPENDANCES ##################################

################### FONCTIONS ##################################
#Fonction TTS : Sauvegarde le fichier sous forme .wav
def textToWavFr(text,file_name):
   subprocess.call(["espeak",text,"-vfr","-w "+file_name+".wav"])
#Fonctionn TTS : Ne garde pas de fichier audio
def textToSpeechFr(text):
   subprocess.call(["espeak",text,"-vfr"])
################### FIN FONCTIONS ##################################
################### PROGRAMME ##################################
### Creation d'un nouveau ChatBot ###
chatbot = ChatBot('Cherry',storage_adapter='chatterbot.storage.JsonFileStorageAdapter',logic_adapters=[{'import_path':'chatterbot.logic.BestMatch'},{'import_path':'chatterbot.logic.LowConfidenceAdapter','threshold':0.6,'default_reponse':'Mon programme ne me permet pas de te raipondre'}],trainer='chatterbot.trainers.ListTrainer')
### FIN Creation d'un nouveau ChatBot ###
### Entrainement du robot ###
#conversation=[question,reponse1,question2,reponse2,...]
chatbot.set_trainer(ListTrainer)
chatbot.train(dialogue)
### FIN Entrainement du robot ###
while True:
    question=input()
    question=str(question)
    try:
    # Taper une des question de la variable 'conversation' entre double cote par exemple "Bonjour"
        if question=="Quelle heure est il":
            importeFichiers("donneesSpatioTemporelles.py")
            subprocess.call('informationsGenerale/donneesSpatioTemporelles.py')
            textToSpeechFr(DonneLHeure())
        if question=="Quel jour sommes nous":
            importeFichiers("donneesSpatioTemporelles.py")
            subprocess.call('informationsGenerale/donneesSpatioTemporelles.py')
            textToSpeechFr(DonneLaDate())
        else:
	        reponse = chatbot.get_response(question)
	        reponse=str(reponse)
	        #print(reponse)
	        textToSpeechFr(reponse)
    except (KeyboardInterrupt, EOFError, SystemExit):
    	break
################### FIN PROGRAMME ##################################
