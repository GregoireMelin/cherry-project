from nose.tools import *
import cherryProject

def setup():
    print "Chargement du fichier setup"

def teardown():
    print "Setup interrompu"

def test_basic():
    print "Lancement du projet"
