#!/usr/bin/env python3
"""
This module contains FileStorage class and it related
attributes and method that dumps python's object into
json file, loads json strings to python's object feom a json
file
"""
import json


class FileStorage():
    """ Class that handles the storage of python's instance attributes
    in a file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the the objects of all instances stored in `__objects`
        """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in objs value with the key obj.id into the '__objects'
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""

        saved = FileStorage.__objects
        filename = self.__class__.__file_path
        with open(filename, 'w', encoding='utf-8') as file:
            obj = {key: value.to_dict() for key, value in saved.items()}
            json.dump(obj, file)

    def reload(self):
        """ deserialize the content of json file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.city import City

        classes = {'BaseModel': BaseModel,
                   'User': User,
                   'State': State,
                   'Amenity': Amenity,
                   'Place': Place,
                   'Review': Review,
                   'City': City}

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:

                contents = json.load(file)
                for key, value in contents.items():
                    class_name = value['__class__']
                    obj = classes[class_name](**value)
                    self.__class__.__objects[key] = obj
        except FileNotFoundError:
            pass
