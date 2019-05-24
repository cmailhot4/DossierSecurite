import socket
from threading import Thread


def thread_recevoir_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        print("[*] Received: %s" %request.decode("utf-8"))


def accepter_client():
    while True:
        client, addr = server.accept()
        clients.append(client)
        print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
        recevoir = Thread(target=thread_recevoir_client, args=(client, ))
        recevoir.start()

def envoyer(texte):
    for client in clients:
        client.send(str.encode(texte))


clients = []
bind_ip = "192.168.60.7"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("Le serveur attend une connexion")

accepte = Thread(target=accepter_client)
accepte.start()

while True:
    texte = input()
    envoyer(texte)



