import threading
from colorama import Fore
from utils import recv
import pickle
from config import (
    BUFFER_SIZE,
    RECV_TIMEOUT
)

class ServerSocketThread(threading.Thread):

    def __init__(self, connection, client_info, \
        buffer_size = BUFFER_SIZE, recv_timeout = RECV_TIMEOUT):

        threading.Thread.__init__(self)
        self.connection = connection
        self.client_info = client_info
        self.buffer_size = buffer_size
        self.recv_timeout = recv_timeout



    def run(self):

        while True :
            received_data, status = recv(self.connection)

            if status == 0:
                self.connection.close()
                print(Fore.RED+f"Connection Closed either due to inactivity for {RECV_TIMEOUT} seconds or due to an error.\n")
                break

            print(Fore.WHITE+f"\nReceived data from the client: ", end="")
            print(Fore.GREEN+f"{received_data}")
            
            msg = "Reply from the server."
            msg = pickle.dumps(msg)
            self.connection.sendall(msg)
            print(Fore.GREEN+"\nServer sent a message to the client.")
            print(Fore.CYAN+f"\nConnection is closed with: {self.client_info}.")