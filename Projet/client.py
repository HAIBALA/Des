import socket
import logging
import traceback
import projet

messegNum = 0
publicKey = ""

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.connect( ('localhost', 9090))

    # Debut de la session
    socket.send('hello')
    chunk = socket.recv(2048)
    messegNum  = messegNum +1
    if messegNum == 1 :

        #recuperation de la cle publique du serveur
        publicKey = chunk
        # generation de la cle DES
        desKey = projet.generateDESKey(64)
        # chiffrement RSA de la cle DES avec la cle publique du serveur
        desKeyEncrypted = desKey.to01()
        # envoi de la cle DES chiffre
        socket.send(desKeyEncrypted)
    # rec
    print "Connection OK"

except Exception as e:
    print logging.error(traceback.format_exc())

