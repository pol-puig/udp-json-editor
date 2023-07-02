import socket
from json_handler.json_operators import JsonReader
from interface import console_interface as con
import logging
import json

def get_json_data():
    """Gets data from a JSON file and stores it in a class.

    Returns:
        JsonReader: An initialized instance with json attributes and path to file

    Raises:
        FileNotFoundError: If the path is incorrect
    """
    # Keeps asking the user for a path to the file until it is correct
    while True:
        try:
            json_path = con.get_user_json_path()
            json_data = JsonReader(json_path)
            break
        except FileNotFoundError:
            print("Error: invalid path")
    return json_data

def get_udp_message(json_data):
    """Transforms JSON attributes and path into an encoded message for UDP communication

    Args:
        json_data: Instance of JsonReader to encode its attributes

    Returns:
        bytes: Encoded attribute message
    """
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


