#!/usr/bin/python3
"""Defines the FileStorage class for HBnB project."""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """A class that serializes instances to JSON file and deserializes back."""
    
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns all objects, or all objects of a class."""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds an object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for k, v in obj_dict.items():
                cls_name = v['__class__']
                self.__objects[k] = eval(cls_name)(**v)
        except FileNotFoundError:
            pass

    def close(self):
        """Deserializes JSON file to objects."""
        self.reload()
