# Imports

import socket
import pickle
from colorama import Fore
from config import (
    BUFFER_SIZE,
    SERVER_HOST,
    SERVER_PORT,
    SOCKET_FAMILY,
    SOCKET_TYPE
)

# Client begins here

soc = socket.socket(
    family = SOCKET_FAMILY,
    type = SOCKET_TYPE
)

soc.connect((
    SERVER_HOST, SERVER_PORT
))
print(Fore.CYAN+"Connected to the server.")

msg = "A message from the client."
msg = pickle.dumps(msg)
soc.sendall(msg)
print(Fore.GREEN+"\nClient sent a message to the server.")

received_data = soc.recv(BUFFER_SIZE)
received_data = pickle.loads(received_data)
print(Fore.WHITE+f"\nReceived data from the server: ", end="")
print(Fore.GREEN+f"{received_data}")

soc.close()
print(Fore.GREEN+"\nSocket is closed.")
print(Fore.WHITE+" ")