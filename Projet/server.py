import  socket


messageNum=0


s = socket.socket()
s.bind(('', 9090))
s.listen(5)
print "socket is listening"


while True:
    # Establish connection with client.
    c, addr = s.accept()
    print 'Got connection from', addr
    chunk = c.recv(2048)
    messageNum = messageNum +1


    if(messageNum ==1 and chunk == 'hello') :
        print  "Envoi de la cle publique"
        c.send('cheikh')
    else :
        if(messageNum == 2) :
            # recption de la cle DES chiffre
            # Dechifrement de la cle DES chiffre
            # envoie un aquitement au client
            c.send('ok')
        else :
            # recption d'un message
            # dechfirement du message avec la cle DES
            # affichage du message sur la sortie standard
            print chunk
    # Close the connection with the client

    c.close()