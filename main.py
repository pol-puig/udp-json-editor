"""
Thread management. It configures 2 threads and starts them. Program finishes when both threads end their execution
"""

import json
import threading
from udp_communication import udp_client, udp_server
import logging

# Host address and port used for communication between threads
ADDRESS = "localhost"
PORT = 8000

def main():
    """It configures 2 threads and starts them. Program finishes when both threads end their execution"""
    # Server thread configuration
    mutex = threading.Lock()  # Create mutex lock for locking data while modifying the json file
    server_thread = threading.Thread(target=udp_server.udp_json_modifier, args=(ADDRESS, PORT, mutex))
    server_thread.daemon = True  # If main thread finishes, server thread will do too
    logging.info("Starting server thread...")
    server_thread.start()

    # Client thread configuration
    client_thread = threading.Thread(target=udp_client.udp_json_sender, args=(ADDRESS, PORT))
    client_thread.daemon = True  # If main thread finishes, client thread will do too
    logging.info("Starting client thread...")
    client_thread.start()

    # Wait for both threads to finish their execution
    client_thread.join()
    server_thread.join()

if __name__ == '__main__':
    main()