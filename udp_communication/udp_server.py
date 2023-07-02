import socket
import json
import threading
from json_handler.json_operators import JsonModifier
from interface import console_interface as con

def receive_data(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    data, addr = server_socket.recvfrom(1024)
    server_socket.close()
    return data

def decode_data(data):
    decoded_data = json.loads(data.decode())
    json_path = decoded_data.pop("json_path")
    return JsonModifier(json_path, decoded_data)

def override_file(json_data):
    user_choice = con.get_save_file_choice()
    if user_choice == "y":
        json_data.save_file()


def udp_json_modifier(host, port, mutex):

    encoded_data = receive_data(host, port)

    json_data = decode_data(encoded_data)

    with mutex:
        while True:
            possible_groups = json_data.get_groups()
            chosen_group = con.get_group_to_modify(possible_groups)


            possible_ids = json_data.get_group_ids(chosen_group)
            chosen_id = con.get_id_to_modify(possible_ids)
            chosen_id_index = possible_ids.index(int(chosen_id))

            possible_attributes = json_data.get_group_attributes(chosen_group, chosen_id_index)
            chosen_attribute = con.get_attribute_to_modify(possible_attributes)


            new_value = con.get_new_value()
            json_data.change_attribute_value(chosen_group, chosen_id_index, chosen_attribute, new_value)

            print(json_data)
            override_file(json_data)

            con.make_more_modifications()





