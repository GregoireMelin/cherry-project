from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def CreationBaseDeConversation(fichierDialogue):
	fichier=open(fichierDialogue,'r')
	lignes=fichier.readlines()
	conversation=['Jaime les pizzas','Moi aussi']
	#ENTRAINEMENT DU CHATBOT
	i=0
	for ligne in lignes:
		conversation.append(ligne[0:-1])

	return(conversation)


chatbot = ChatBot('Cherry',storage_adapter='chatterbot.storage.JsonFileStorageAdapter',logic_adapters=[{'import_path':'chatterbot.logic.BestMatch'},{'import_path':'chatterbot.logic.LowConfidenceAdapter','threshold':0.6,'default_reponse':'Mon programme ne me permet pas de te raipondre'}],trainer='chatterbot.trainers.ListTrainer')
chatbot.set_trainer(ListTrainer)
dialogue=CreationBaseDeConversation('dialogue_general.txt')
chatbot.train(dialogue)
