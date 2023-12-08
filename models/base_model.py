#!/usr/bin/python3
import uuid
from datetime import datetime

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


class BaseModel:
    """
    Base class for models.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is not empty:
            - Each key of the dictionary is an attribute name.
            - Each value of the dictionary is the value of
            the attribute with the corresponding name.
            - The 'created_at' and 'updated_at' attributes are
            converted from strings to datetime objects.

        If kwargs is empty:
            - An 'id' attribute is generated.
            - A 'created_at' attribute is set to the current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save

    def to_dict(self):
        """
        Convert the BaseModel instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            str: String representation of the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    @classmethod
    def from_dict(cls, data):
        """create a new instance of BaseModel"""
        obj = cls()
        for key, value in data.items():
            if key == '__class__':
                continue
            setattr(obj, key, value)
            if key == 'created_at' or key == 'updated_at':
                setattr(obj, key, datetime.strptime(value,
                                                    '%Y-%m-%dT%H:%M:%S'))
        return obj
