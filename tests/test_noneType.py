from interactions import ReconnaissanceVocaleGoogle
from interactions import Repondre
import utilisateur
import dateEtHeure
import vdm
import random
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

req=ReconnaissanceVocaleGoogle()
if req==None:
    Repondre('Je n" ai pas compris la question')
else:
    Repondre('Test positif !')
