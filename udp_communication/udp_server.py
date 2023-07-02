"""
Handles JSON data received from a UDP connection depending on user choices
"""

import socket
import json
import threading
import logging
from json_handler.json_operators import JsonModifier
from interface import console_interface as con

BUFFER_SIZE = 2048  # Buffer size for data reception

def receive_data(host, port):
    """Opens a socket to receive data and closes it afterwards

    Args:
        host: Host address
        port: Port for the communication

    Returns:
        bytes: Encoded data received from a client

    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Set IPv4 and UDP
    server_socket.bind((host, port))
    logging.info("Listening socket created")
    data, addr = server_socket.recvfrom(BUFFER_SIZE)  # Listen until data is received
    logging.info("Data received")
    server_socket.close()  # Close socket when data is received
    logging.info("Listening socket closed")
    return data

def decode_json_data(data):
    """Decode data and store it in a JsonModifier instance

    Args:
        data: Data to be decode in bytes

    Returns:
        JsonModifier: Initialized instance with json attributes and path to source file
    """
    decoded_data = json.loads(data.decode())
    json_path = decoded_data.pop("json_path")
    return JsonModifier(json_path, decoded_data)

def override_json_file(json_data):
    """Saves file at the same path where it was read only if user chooses the option

    Args:
        json_data: Instance containing the attributes to save
    """
    user_choice = con.get_save_file_choice()

    # Only overrides file if user wants
    if user_choice == "y":
        json_data.save_file()
        logging.info("File has been successfully overwritten")


def udp_json_modifier(host, port, mutex):
    """Receives JSON data and modifies it according to user inputs

    Args:
        host: Host address
        port: Port for the communication
        mutex: Thread lock
    """
    # Receive and decode JSON data
    encoded_data = receive_data(host, port)
    json_data = decode_json_data(encoded_data)

    # Lock block of code while executing
    with mutex:
        while True:
            # Get chosen group to modify from the user. The group is among the possible groups
            possible_groups = json_data.get_groups()
            chosen_group = con.get_group_to_modify(possible_groups)

            # Get chosen id list index to modify from the user, only from the possible options
            possible_ids = json_data.get_group_ids(chosen_group)
            chosen_id = con.get_id_to_modify(possible_ids)
            chosen_id_index = possible_ids.index(int(chosen_id))

            # Get chosen attribute to modify from the user, only from the possible options
            possible_attributes = json_data.get_group_attributes(chosen_group, chosen_id_index)
            chosen_attribute = con.get_attribute_to_modify(possible_attributes)

            # Get user's new value for the attribute, changes it and shows resulting change
            new_value = con.get_new_value()
            json_data.change_attribute_value(chosen_group, chosen_id_index, chosen_attribute, new_value)
            print(json_data)

            # Override json file and make more modifications, if user wants
            override_json_file(json_data)
            con.make_more_modifications()