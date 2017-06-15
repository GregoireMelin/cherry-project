from interactions import *
import utilisateur
import dateEtHeure
import random
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Initialisation de la variable de session
Session=True

#Initialisation du chatbot
chatbot = ChatBot('Cherry',storage_adapter='chatterbot.storage.JsonFileStorageAdapter',logic_adapters=[{'import_path':'chatterbot.logic.BestMatch'},{'import_path':'chatterbot.logic.LowConfidenceAdapter','threshold':0.6,'default_reponse':'Je ne sais pas'}],trainer='chatterbot.trainers.ListTrainer')
chatbot.set_trainer(ListTrainer)
dialogue=CreationBaseDeConversation('dialogue_general.txt')
chatbot.train(dialogue)

#Demarrage
if utilisateur.administrateur==True:
    Repondre('Connexion administrateur'+utilisateur.nom)
else:
    Repondre('Connexion'+utilisateur.prenom)

#Dicussion
while Session==True:
	#Prise de son : On releve ce que dit l'utilisateur
	debutTransmission()
	requete=ReconnaissanceVocaleGoogle()
	if not requete==None:

		print("Tu as dit : ")
		finTransmission()
		print(requete)
		if " heure" in requete:
			h=dateEtHeure.DonneLHeure()
			print("Cherry : ")
			print(h)
			Repondre(h)

		elif " date" in requete or " jour" in requete:
			d=dateEtHeure.DonneLaDate()
			print("Cherry : ")
			print(d)
			Repondre(d)

		elif "blague" in requete:
			Vdms=getVDM()
			Vdm=Vdms[random.randint(0, len(Vdms)-1)]
			print("Cherry : ")
			print(Vdm)
			Repondre(Vdm+'V D M')

		elif requete=="parle-moi":
			import discussionFoot

		elif "fin de la discussion" in requete:
			print("Cherry : ")
			print("Merci de la dicussion")
			Repondre('Merci de la discussion')
			print("Au revoir")
			Repondre('Au revoir')
			Session=False
		else:
			if str(chatbot.get_response(requete))=="I'm sorry, I do not understand.":
				Repondre('Je ne comprend pas la demande')
				print("Cherry : ")
				print("Je ne comprend pas la demande")
			else:
				Repondre(str(chatbot.get_response(requete)))
				print("Cherry : ")
				print(str(chatbot.get_response(requete)))
