#!/usr/bin/python3
"""
FileStorage class
"""

import json
import os


from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State
    }


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = os.path.join(os.path.dirname(__file__), "file.json")
    # empty dictionary to store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                json_data = json.load(f)
            for key, value in json_data.items():
                class_name, obj_id = key.split('.')
                if class_name in classes:
                    cls = classes[class_name]
                    self.__objects[key] = cls(**value)
                else:
                    print(f"Unknown class '{class_name}' encountered in JSON.")
        except FileNotFoundError:
            pass
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in {self.__file_path}: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
