#!/usr/bin/python3
import json
import importlib


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        obj_dict = {key: value.to_dict()
                    for key, value in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects.
        Only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesnt exist, no exception should be raised.
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    module = importlib.import_module(f'models.{class_name}')
                    cls = getattr(module, class_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            # Handle JSON decoding errors (invalid JSON)
            print(f"Error decoding JSON in {self.__file_path}")
