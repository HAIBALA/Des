import  socket
s = socket.socket()
s.bind(('', 9090))
s.listen(5)
print "socket is listening"


while True:
    # Establish connection with client.
    c, addr = s.accept()
    print 'Got connection from', addr

    # send a thank you message to the client.
    c.send('Thank you for connecting')

    # Close the connection with the client
    c.close()