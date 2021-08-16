# Imports

import socket
from utils import recv 
from colorama import Fore
import pickle
from config import (
    BUFFER_SIZE, 
    SERVER_ACCEPT_TIMEOUT, 
    SERVER_HOST, 
    SERVER_INCOMING_LIMIT, 
    SERVER_PORT, 
    SOCKET_FAMILY, 
    SOCKET_TYPE,
    RECV_TIMEOUT
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

soc.settimeout(SERVER_ACCEPT_TIMEOUT)
connected = False
try:
    connection, address = soc.accept()
    print(Fore.GREEN + f"Connected to a client: {address}.")
    connected = True
except socket.timeout:
    print(Fore.RED + "The server socket has timed out.")
    soc.close()

if connected:
    while True :
        received_data, status = recv(connection)
        if status == 0:
            connection.close()
            print(Fore.RED+f"Connection Closed either due to inactivity for {RECV_TIMEOUT} seconds or due to an error.\n")
            break
        print(Fore.WHITE+f"\nReceived data from the client: ", end="")
        print(Fore.GREEN+f"{received_data}")
        
        msg = "Reply from the server."
        msg = pickle.dumps(msg)
        connection.sendall(msg)
        print(Fore.GREEN+"\nServer sent a message to the client.")
    print(Fore.CYAN+f"\nConnection is closed with: {address}.")

soc.close()
print(Fore.GREEN+"\nSocket is closed.")
print(Fore.WHITE+" ")