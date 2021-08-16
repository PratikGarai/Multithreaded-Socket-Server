# Imports

from implementations.ServerSockerThread import ServerSocketThread
import socket
from utils import recv 
from colorama import Fore
from config import (
    SERVER_ACCEPT_TIMEOUT, 
    SERVER_HOST, 
    SERVER_INCOMING_LIMIT, 
    SERVER_PORT, 
    SOCKET_FAMILY, 
    SOCKET_TYPE,
)

# Server starts here

soc = socket.socket(
    family = SOCKET_FAMILY,
    type = SOCKET_TYPE
)

soc.bind((
    SERVER_HOST,
    SERVER_PORT
))
print(Fore.CYAN + f"Socket is bound to {SERVER_HOST} on port {SERVER_PORT}.")

soc.listen(SERVER_INCOMING_LIMIT)
print(Fore.CYAN + "Listening for incoming connection ...")

while True : 

    soc.settimeout(SERVER_ACCEPT_TIMEOUT)
    try:
        connection, address = soc.accept()
        print(Fore.GREEN + f"Connected to a client: {address}.")
        socket_thread = ServerSocketThread(connection, address)
        socket_thread.start()
    
    except socket.timeout:
        print(Fore.RED + "The server socket has timed out.")
        soc.close()
        break

print(Fore.GREEN+"\nSocket is closed.")
print(Fore.WHITE+" ")