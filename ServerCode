# importing the socket library to use
import socket
import sys
from math import *
import logging
import threading

# define constants
HEADER = 64
HOST = "127.0.01"
PORT = 8080 #select port number with no other use
FORMAT = 'utf-8'
ADDRESS = (HOST, PORT)

TK_SILENCE_DEPRECATION=1

# create an instance of a socket and assign a port and IP addr to it
gServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gServer.bind(ADDRESS)
msg = ''

DISCON_MSG = "!DISCONNECT!"

# Create an object for the logger
logger = logging.getLogger("Calculator Logger")
# Set the level of the logging
logger.setLevel(logging.INFO)
# Create a file handler to log the messages to a file and set logging level
file_handler = logging.FileHandler("calculator.log")
file_handler.setLevel(logging.INFO)
# Create a formatter to specify the formatting of the log messages
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
# Add the file handler to the logger
logger.addHandler(file_handler)


# function which handles the receiving of the message by running an infinite loop
# to decode the message and print it
# if the disconnect message is sent then the loop exits and the server disconnects
def receive():
    gServer.listen()
    # Establish connection between client and server
    connectionToClient, clientAddress = gServer.accept()
        
    connected = True
    while connected:
        try:
            data = connectionToClient.recv(1024)
            msg = data.decode()
            operator = msg
            result = str(eval(operator))
            connectionToClient.send(result.encode())
            logger.info("Evaluated expression '%s' to get %s", operator, result)
        except:
            connectionToClient.send("Invalid expression".encode())

        

print("Server starting.....")
receive()
