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
    RepondreESpeakStreaming('Connexion administrateur'+utilisateur.nom)
else:
    RepondreESpeakStreaming('Connexion'+utilisateur.prenom)

#Dicussion
while Session==True:
	#Prise de son : On releve ce que dit l'utilisateur
	requete=ReconnaissanceVocaleGoogle()
	if not requete==None:

		print("Tu as dit : ")
		finTransmission()
		print(requete)
		print("Cherry : ")
		#Traitement de la requete
		if "introduit toi" in requete :
			print("Je suis Cherry, robot mis a disposition des enfants pour passer le temps.")
			RepondreESpeakStreaming('Je suis Cherry, robot mis a disposition des enfants pour passer le temps.')
        	#RepondreESpeakStreaming('Mon concepteur est lassociation Prima et mon module de discussion est fait par Monsieur Melin')
        	#RepondreESpeakStreaming('Dans le cadre de son projet informatique individuel de Bordeaux I N P E N S C ')
		elif " heure" in requete:
			h=dateEtHeure.DonneLHeure()
			print(h)
			RepondreESpeakStreaming(h)

		elif " date" in requete or " jour" in requete:
			d=dateEtHeure.DonneLaDate()
			print(d)
			RepondreESpeakStreaming(d)
		elif "l'explication de la vie" in requete:
			print("L'explication de la grande question de la vie, de l'univers et de tout le reste est 42")
			RepondreESpeakStreaming('Lexplication de la grande question de la vie, de lunivers et de tout le reste est 42')

		elif " blague" in requete:
			Vdms=getVDM()
			Vdm=Vdms[random.randint(0, len(Vdms)-1)]
			print(Vdm)
			RepondreESpeakStreaming(Vdm+'V D M')

		elif requete=="fin de la discussion":
			print("Merci de la dicussion")
			RepondreESpeakStreaming('Merci de la discussion')
			print("Au revoir")
			RepondreESpeakStreaming('Au revoir')
			Session=False
		else:
			if str(chatbot.get_response(requete))=="I'm sorry, I do not understand.":
				RepondreESpeakStreaming('Je ne comprend pas la demande')
				print("Je ne comprend pas la demande")
			else:
				RepondreESpeakStreaming(str(chatbot.get_response(requete)))
				print(str(chatbot.get_response(requete)))
