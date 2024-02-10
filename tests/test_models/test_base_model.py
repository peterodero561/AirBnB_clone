#!/usr/bin/python3
'''tests cases for the BaseModel class'''
import unittest
import datetime
from datetime import timedelta
import uuid
import json
from models.base_model import BaseModel
from models import storage


class test_BaseModel(unittest.TestCase):
    '''class containing all the function test cases'''
    def setUp(self):
        '''Does the setup'''
        self.base_model = BaseModel()

    def test_initialization(self):
        '''
        checks if id is string
        checks if "created_at" and "update_at" are datetime objects
        verifys that "created_at" and "update_at" are close to current time
        checks if the object is added to the storage
        '''
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)
        self.assertAlmostEqual(
                self.base_model.created_at,
                datetime.datetime.now(),
                delta=timedelta(seconds=1)
                )
        self.assertAlmostEqual(
                self.base_model.updated_at,
                datetime.datetime.now(),
                delta=timedelta(seconds=1)
                )
        self.assertIn(self.base_model, storage.all().values())

    def test_initialization_with_specific_parameters(self):
        '''checks initalization with specific parameters'''
        specific_created_at = datetime.datetime(2022, 1, 1)
        specific_updated_at = datetime.datetime(2022, 1, 2)
        specific_base_model = BaseModel(
                created_at=specific_created_at, updated_at=specific_updated_at)
        self.assertEqual(specific_base_model.created_at, specific_created_at)
        self.assertEqual(specific_base_model.updated_at, specific_updated_at)

    def test_str_method(self):
        '''test what __str__() returns'''
        expected_str = (
                f"[{self.base_model.__class__.__name__}] "
                f"({self.base_model.id}) "
                f"{self.base_model.__dict__}"
                )
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        '''checks whether updated_at is always updated'''
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)
        self.assertIn(self.base_model, storage.all().values())

    def test_to_dict_method(self):
        '''checks whether the to_dict method saves the in a dictionary form'''
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': self.base_model.__class__.__name__
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)

    def test_from_dict_method(self):
        '''test the from_dict()'''
        dict_obj = self.base_model.to_dict()
        new_instance = BaseModel.from_dict(dict_obj)
        self.assertIsInstance(new_instance, BaseModel)
        self.assertEqual(new_instance.id, self.base_model.id)
        self.assertEqual(new_instance.created_at, self.base_model.created_at)
        self.assertEqual(new_instance.updated_at, self.base_model.updated_at)

    def test_multiple_instances(self):
        '''checks whether id is different at each instance of BaseModel'''
        another_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, another_base_model.id)
        self.assertIn(another_base_model, storage.all().values())

    def test_str_method_with_custom_attributes(self):
        '''testing __str__() with attributes'''
        custom_base_model = BaseModel()
        custom_base_model.custom_attribute = "test"
        expected_str = (
            f"[{custom_base_model.__class__.__name__}] "
            f"({custom_base_model.id}) "
            f"{custom_base_model.__dict__}"
        )
        self.assertEqual(str(custom_base_model), expected_str)

    def test_save_method_multiple_times(self):
        '''checks updated_at is updated after multiple times'''
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

        old_updated_at = self.base_model.updated_at
        # Simulate delay
        import time
        time.sleep(1)
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_serialization_deserialization(self):
        '''test serialization and deserialization'''
        serialized_data = json.dumps(self.base_model.to_dict())
        deserialized_data = json.loads(serialized_data)
        new_instance = BaseModel.from_dict(deserialized_data)
        self.assertIsInstance(new_instance, BaseModel)
        self.assertEqual(new_instance.id, self.base_model.id)
        self.assertEqual(new_instance.created_at, self.base_model.created_at)
        self.assertEqual(new_instance.updated_at, self.base_model.updated_at)

    @unittest.skip("Example of skipped test")
    def test_skip_example(self):
        self.assertTrue(False)
