"""
It shows in console the required steps for the user to use the program. It also handles his inputs.
"""
import sys

DEFAULT_JSON_PATH="./data/udp.json"

def get_user_json_path():
    """Gets user path to json file from console input.

    Returns:
        str: User chosen path
    """
    path = input("Please, provide a valid path to a json file. Press enter to use default path (../data/udp.json)\n")

    # If no path is provided, use default path
    if path == '':
        return DEFAULT_JSON_PATH
    else:
        return path

def get_item_to_modify(possible_items):
    """Gets the item that the user wants to modify.

    Args:
        possible_items: List that contains only the possible modificable items

    Returns:
        str: User inputed choice
    """
    for item in possible_items:
        print("  " + item)  # Print each of the possible items to be modified

    # Return user input only when it is a possible item
    while True:
        user_choice = input()
        if user_choice in possible_items:
            return user_choice
        else:
            print("Invalid input. Please, make sure there are no typos")

def get_group_to_modify(possible_groups):
    """Gets the group that the user wants to modify (e.g. 'cars') only when it is an existing group.

    Args:
        possible_groups: List that contains only the possible modificable groups

    Returns:
        str: Group to modify
    """
    print("Please, write the name of the group that should be modified: ")
    return get_item_to_modify(possible_groups)

def get_id_to_modify(possible_ids):
    """Gets the id that the user wants to modify (e.g. 1) only when it is an existing id.

    Args:
        possible_ids: List that contains only the possible modificable ids

    Returns:
        str: Id to modify
    """
    print("Please, write the id of the element that should be modified: ")
    possible_ids = list(map(str, possible_ids))  #Transform indexes into strings
    return get_item_to_modify(possible_ids)

def get_attribute_to_modify(possible_attributes):
    """Gets the attribute that the user wants to modify (e.g. "brand") only when it is an existing attribute.

    Args:
        possible_attributes: List that contains only the possible modificable attributes

    Returns:
        str: Attribute to modify
    """
    print("Please, write the name of the attribute that should be modified: ")
    return get_item_to_modify(possible_attributes)

def get_new_value():
    """Gets the value that the user wants to set in an attribute

    Returns:
        str: User desired new attribute value
    """
    return input("Please, provide a new value for the selected attribute. If it is an id, it must be an unique integer\n")

def get_save_file_choice():
    """Gets user decision when asked to override the json file that is being edited.

    Returns:
        str: A 'y' or a 'n' depending on user input
    """
    print("Would you like to save the edited json?. Warning: this action will override the old json file")

    # Only 'y' or 'n' can be inputed. Otherwise, ask again for a correct input
    while True:
        choice = input("Choose: 'y' or 'n'\n")
        if choice in ["y", "n"]:
            return choice
        else:
            print("Invalid input. Please, write 'y' or 'n'\n")

def make_more_modifications():
    """If users wants to make more modifications, do nothing. Otherwise, exit thread"""
    print("Would you like to make more modifications? ('n' will exit the program)")

    # Input should be 'y' or 'n'. Ask for it until the input is correct
    while True:
        choice = input("Choose: 'y' or 'n'\n")
        if choice == "y":
            break
        elif choice == "n":
            sys.exit(0)
        else:
            print("Invalid input. Check for typos\n")