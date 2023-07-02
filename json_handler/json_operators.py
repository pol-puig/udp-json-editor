"""
This module contains all required classes and methods for proper json handling.
"""

import json

class JsonReader:
    """Loads a json file attributes and its path

    """

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
    def __init__(self, path, attributes):
        self.path = path
        self.attributes = attributes

    def get_groups(self):
        return self.attributes.keys()

    def get_group_ids(self, group):
        group_ids = []
        for item in self.attributes[group]:
            group_ids.append(item["id"])
        return group_ids

    def get_group_attributes(self, group, id_index):
        return self.attributes[group][id_index].keys()

    def change_attribute_value(self, group, id_index, attribute, new_value):
        self.attributes[group][id_index][attribute] = new_value

    def save_file(self):
        with open(self.path, 'w') as file:
            json.dump(self.attributes, file)

    def __str__(self):
        """Represents class as an easy to-read string version of all stored json attributes

            Returns:
                str: All attributes with indentation
        """
        return json.dumps(self.attributes, indent=2, ensure_ascii=False)
