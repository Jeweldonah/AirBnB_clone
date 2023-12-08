#!/usr/bin/python3
import unittest
import os
import tempfile
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing storage
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_filename = self.temp_file.name

        # Set up FileStorage with the temporary file
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.temp_filename
        self.storage.reload()

    def tearDown(self):
        # Close and remove the temporary file
        self.temp_file.close()
        os.remove(self.temp_filename)

    def test_init_method(self):
        """
        Test the '__init__' method of the BaseModel class.
        """
        # Create a BaseModel instance
        base_model = BaseModel()

        # Ensure the instance is added to the storage
        self.assertIn(base_model, self.storage.all().values())

    def test_save_method(self):
        """
        Test the 'save' method of the BaseModel class.
        """
        # Create a BaseModel instance
        base_model = BaseModel()

        # Update the instance and save it
        base_model.save()

        # Reload the storage and check if the instance is present
        self.storage.reload()
        self.assertIn(base_model, self.storage.all().values())

    def test_to_dict_method(self):
        """
        Test the 'to_dict' method of the BaseModel class.
        """
        # Create a BaseModel instance
        base_model = BaseModel()

        # Convert the instance to a dictionary
        obj_dict = base_model.to_dict()

        # Check if the dictionary contains expected keys
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

    def test_str_method(self):
        """
        Test the '__str__' method of the BaseModel class.
        """
        # Create a BaseModel instance
        base_model = BaseModel()

        # Convert the instance to a string
        obj_str = str(base_model)

        # Check if the string representation contains expected information
        self.assertIn(base_model.id, obj_str)
        self.assertIn(base_model.__class__.__name__, obj_str)

    def test_from_dict_method(self):
        """
        Test the 'from_dict' class method of the BaseModel class.
        """
        # Sample data for testing
        base_model_data = {
            '__class__': 'BaseModel',
            'id': 'test_id',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T01:00:00',
            'custom_attribute': 'custom_value'
        }

        # Create a BaseModel instance from the provided dictionary
        base_model = BaseModel.from_dict(base_model_data)

        # Ensure the returned object is an instance of BaseModel
        self.assertIsInstance(base_model, BaseModel)

        # Check if attributes are set correctly
        self.assertEqual(base_model.id, 'test_id')
        self.assertEqual(base_model.custom_attribute, 'custom_value')
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
