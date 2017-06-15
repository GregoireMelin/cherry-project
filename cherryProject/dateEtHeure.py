#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import struct
import time

import locale
locale.setlocale(locale.LC_TIME,'')

def DonneLHeure(sntp='ntp.univ-lyon1.fr'):
        """tempsntp(sntp='ntp.univ-lyon1.fr'): Donne la date et l'heure exacte par consultation d'un serveur ntp"""
        jsem=["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
        mannee=["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
        temps19701900 = 2208988800L
        buffer=1024
        # initialisation d'une connexion UDP
        client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # envoie de la requête UDP
        data='\x1b' + 47 * '\0'
        client.sendto(data, (sntp, 123))
        # réception de la réponse UDP
        data, addresse = client.recvfrom(buffer)
        if data:
            tps = struct.unpack('!12I', data)[10]
            tps -= temps19701900
            t=time.localtime(tps)
            ch="Il est "+str(t[3]).zfill(2)+" heures "+str(t[4]).zfill(2)
            return ch
        else:
            return "échec: pas de réponse du serveur"

def DonneLaDate(sntp='ntp.univ-lyon1.fr'):
        """tempsntp(sntp='ntp.univ-lyon1.fr'): Donne la date et l'heure exacte par consultation d'un serveur ntp"""
        jsem=["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
        mannee=["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
        temps19701900 = 2208988800L
        buffer=1024
        # initialisation d'une connexion UDP
        client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # envoie de la requête UDP
        data='\x1b' + 47 * '\0'
        client.sendto(data, (sntp, 123))
        # réception de la réponse UDP
        data, addresse = client.recvfrom(buffer)
        if data:
            tps = struct.unpack('!12I', data)[10]
            tps -= temps19701900
            t=time.localtime(tps)
            ch="Nous sommes le "+jsem[t[6]] +" "+str(t[2]).zfill(2)+" "+mannee[t[1]]+" "+str(t[0]).zfill(4)
            return ch
        else:
            return "echec: pas de réponse du serveur"

#ch=jsem[t[6]] = nom du jour
#str(t[2]).zfill(2) = jour
#str(t[1]).zfill(2) = mois
#str(t[0]).zfill(4) = annee
#str(t[3]).zfill(2) = heures
#str(t[4]).zfill(2) = minutes
#str(t[5]).zfill(2) = secondes
