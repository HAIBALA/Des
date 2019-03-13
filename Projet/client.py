import socket
import logging
import  traceback
try :
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect( ('localhost', 80))

except Exception as e:
    print logging.error(traceback.format_exc())

print "Connection OK"

