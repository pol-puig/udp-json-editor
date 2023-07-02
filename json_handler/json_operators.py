"""
This module contains all required classes and methods for proper json handling.
"""

import json

class JsonReader:
    """Handles JSON read-related tasks. Stores JSON attributes from a file and path to the file"""

    def __init__(self, path):
        """Constructor: loads json file attributes and its path

        Args:
            path: Path to the json file
        """
        self.path = path
        self.attributes = self.load_data(path)

    def load_data(self,path):
        """Gets all attributes from a json file

        Args:
            path: Path to the json file

        Returns:
            dict: Attributes from the read json file
        """
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def __str__(self):
        """Represents class as an easy to-read string version of all stored json attributes

        Returns:
            str: All attributes with indentation
        """
        return json.dumps(self.attributes, indent=2, ensure_ascii=False)


class JsonModifier:
    """Handles JSON modify-related tasks. Stores JSON attributes and path to its file"""
    def __init__(self, path, attributes):
        """Constructor: stores json attributes and path to the original file

            Args:
                path: Path to the json file
                attributes: Dictionary with json attributes
        """
        self.path = path
        self.attributes = attributes

    def get_groups(self):
        """Get all first-level (group) keys in JSON (e.g. 'cars')

        Returns:
            list: All first-level keys
        """
        return self.attributes.keys()

    def get_group_ids(self, group):
        """Get all ids within a group (e.g. 'cars' has elements with ids 1,2,3)

            Args:
                group: Key of the group

            Returns:
                list: All group ids
        """
        group_ids = []
        for item in self.attributes[group]:
            group_ids.append(item["id"])
        return group_ids

    def get_group_attributes(self, group, id_index):
        """Get all attribute keys within a group and id (e.g. 'cars' and id=1 has ["id","name","brand"])

            Args:
                group: Key of the group
                id_index: Int representing the position that the id takes in the id list

            Returns:
                list: All attribute keys for a specific group and id
        """
        return self.attributes[group][id_index].keys()

    def change_attribute_value(self, group, id_index, attribute, new_value):
        """Edits the value of a specific attribute

            Args:
                group: Key of the group
                id_index: Int representing the position that the id takes in the id list
                attribute: Key of the value that should be modified
                new_value: Value of the attribute to modify
        """
        self.attributes[group][id_index][attribute] = new_value

    def save_file(self):
        """Save attributes to a new JSON file"""
        with open(self.path, 'w') as file:
            json.dump(self.attributes, file)

    def __str__(self):
        """Represents class as an easy to-read string version of all stored json attributes

            Returns:
                str: All attributes with indentation
        """
        return json.dumps(self.attributes, indent=2, ensure_ascii=False)