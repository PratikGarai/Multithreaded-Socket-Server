# Imports

import socket 
from colorama import Fore
import pickle


# Globals
SOCKET_FAMILY = socket.AF_INET
SOCKET_TYPE = socket.SOCK_STREAM
SOCKET_HOST = "localhost"
SOCKET_PORT = 3500
SOCKET_INCOMING_LIMIT = 1
SOCKET_ACCEPT_TIMEOUT = 5

BUFFER_SIZE = 8         # Bytes

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

soc.settimeout(SOCKET_ACCEPT_TIMEOUT)
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
    print(Fore.GREEN+f"Received data from the client: {received_data}")
    
    msg = "Reply from the server."
    msg = pickle.loads(msg)
    connection.sendall(msg)
    print(Fore.GREEN+"Server sent a message to the client.")

    connection.close()
    print(Fore.CYAN+f"Connection is closed with: {address}.")

soc.close()
print(Fore.GREEN+"\nSocket is closed.")
print(Fore.WHITE)