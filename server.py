# Imports

import socket 
from colorama import Fore
import pickle
from config import (
    BUFFER_SIZE, 
    SERVER_ACCEPT_TIMEOUT, 
    SERVER_HOST, 
    SERVER_INCOMING_LIMIT, 
    SERVER_PORT, 
    SOCKET_FAMILY, 
    SOCKET_TYPE
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
    received_data = connection.recv(BUFFER_SIZE)
    received_data = pickle.loads(received_data)
    print(Fore.WHITE+f"\nReceived data from the client: ", end="")
    print(Fore.GREEN+f"{received_data}")
    
    msg = "Reply from the server."
    msg = pickle.dumps(msg)
    connection.sendall(msg)
    print(Fore.GREEN+"\nServer sent a message to the client.")

    connection.close()
    print(Fore.CYAN+f"\nConnection is closed with: {address}.")

soc.close()
print(Fore.GREEN+"\nSocket is closed.")
print(Fore.WHITE+" ")