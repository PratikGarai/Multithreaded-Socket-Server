# Imports

import socket 
from colorama import Fore


# Globals
SOCKET_FAMILY = socket.AF_INET
SOCKET_TYPE = socket.SOCK_STREAM
SOCKET_HOST = "localhost"
SOCKET_PORT = 3500
SOCKET_INCOMING_LIMIT = 1


# Server starts here

soc = socket.socket(
    family = SOCKET_FAMILY,
    type = SOCKET_TYPE
)

soc.bind((
    SOCKET_HOST,
    SOCKET_PORT
))
print(Fore.CYAN + f"Socket is bound to {SOCKET_HOST} on port {SOCKET_PORT}.")

soc.listen(SOCKET_INCOMING_LIMIT)
print(Fore.CYAN + "Listening for incoming connection ...")

connection, address = soc.accept()
print(Fore.GREEN + f"Connected to a client: {address}.")