#!/usr/bin/python3
import json


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
            # value = obj.to_dict()
            self.__objects[key] = obj

    def save(self):
        """ Serializes objects to JSON file path """
        json_data = {}
        if self.__objects:
            for key, obj in self.__objects.items():
                json_data[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(json_data, file)
            # return obj_json

    def reload(self):
        """ Deserializes the JSON file """

        if self.__file_path:
            try:
                from models.base_model import BaseModel
                with open(self.__file_path, 'r') as file:
                    json_data = file.read()
                dict_from_json = json.loads(json_data)
                for key, obj_dict in dict_from_json.items():
                    obj = eval(obj_dict["__class__"])(
                        **obj_dict)  # get class from its name
                    self.__objects[key] = obj  # Recreate class

            except FileNotFoundError:
                pass
        else:
            pass
