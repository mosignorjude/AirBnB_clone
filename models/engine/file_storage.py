#!/usr/bin/python3
import json


"""Defines a class Filestorage"""


class FileStorage():
    """ Represents a file storage """

    def __init__(self):
        """ initializes a class attributes """

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ Returns __objects """
        return self.__objects

    def new(self, obj):
        """ sets the object dictionary """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            value = obj.to_dict()
            self.__objects[key] = value

    def save(self):
        """ Serializes objects to JSON file path """
        with open(self.__file_path, 'w') as file:
            obj_json = json.dump(self.__objects, file)
            return obj_json

    def reload(self):
        """ Deserializes the JSON file """
        if self.__file_path:
            try:
                with open(self.__file_path, 'r') as file:
                    json_data = file.read()
                my_dict = json.loads(json_data)
                self.__objects = my_dict
            except FileNotFoundError:
                pass
        else:
            pass
