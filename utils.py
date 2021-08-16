import time
import pickle
from colorama import Fore
from config import (
    BUFFER_SIZE,
    RECV_TIMEOUT
)

def recv(connection, buffer_size=BUFFER_SIZE, recv_timeout=RECV_TIMEOUT):
    recv_start_time = time.time() # Time at which last chunk is received from the client.
    received_data = b""
    while True:
        try:
            data = connection.recv(buffer_size)
            received_data += data

            if data == b'': # Nothing received from the client.
                received_data = b""
                # If still nothing received for a number of seconds specified by the recv_timeout attribute, return with status 0 to close the connection.
                if (time.time() - recv_start_time) > recv_timeout:
                    return None, 0 # 0 means the connection is no longer active and it should be closed.
            elif str(data)[-2] == '.':
                print(Fore.YELLOW+f"All data {len(received_data)} bytes) Received.")

                if len(received_data) > 0:
                    try:
                        # Decoding the data (bytes).
                        received_data = pickle.loads(received_data)
                        # Returning the decoded data.
                        return received_data, 1

                    except BaseException as e:
                        print(Fore.RED+f"Error Decoding the Client's Data: {e}.\n")
                        return None, 0
            else:
                # In case data are received from the client, update the recv_start_time to the current time to reset the timeout counter.
                recv_start_time = time.time()

        except BaseException as e:
            print(Fore.RED+f"Error Receiving Data from the Client: {e}.\n")
            return None, 0