import socket
import json
import threading
from json_handler.json_operators import JsonReader
from interface import console_interface as con
import logging

def get_json_data():
    while True:
        try:
            json_path = con.get_user_json_path()
            json_data = JsonReader(json_path)
            break
        except FileNotFoundError:
            print("Error: invalid path")
    return json_data

def get_udp_message(json_data):
    message = json_data.attributes
    message["json_path"] = json_data.path
    message = json.dumps(message, ensure_ascii=False).encode()
    return message

def udp_json_sender(host, port):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    logging.info("Client socket successfully created")

    json_data = get_json_data()
    udp_message = get_udp_message(json_data)

    client_socket.sendto(udp_message, (host, port))
    logging.info("Thread1 sent message to thread2 successfully")


    client_socket.close()


