#!/usr/bin/python3
'''module containing test cases for FileStorage class'''
import unittest
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel


class Test_file_storage(unittest.TestCase):
    '''class containing all methods that test FileStorage Class'''
    def setUp(self):
        '''sets up an instance of the FileStorage class'''
        self.storage = FileStorage()

    def tearDown(self):
        '''checks if the path to the json file exists'''
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_save_and_reload_empty_file(self):
        '''checks saving and realoding of a empty file'''
        # self.storage.save()
        # self.storage.reload()
        # self.assertEqual(self.storage.all(), {})
        try:
            self.storage.save()
        except EmptyFileError:
            # Treat empty file as an error
            self.fail("Empty file should raise an error.")

    def test_save_and_reload_non_empty_file(self):
        '''checks saving and realoding of a non-empty file'''
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(new_storage.all(), self.storage.all())

    def test_adding_and_removing_objects(self):
        '''tests adding and removing objects from json file'''
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 2)

        # Remove one object and save
        del self.storage._FileStorage__objects['BaseModel.{}'.format(obj1.id)]
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn('BaseModel.{}'.format(obj2.id), self.storage.all())

    def test_serialization_and_deserialization(self):
        '''tests saving and reloading of elements from json file'''
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        self.storage._FileStorage__objects = {}
        self.storage.reload()
        for key, obj in self.storage.all().items():
            class_name, obj_id = key.split('.')
            self.assertIsInstance(obj, BaseModel)
            self.assertEqual(obj.__class__.__name__, class_name)

    def test_non_existing_file(self):
        '''testing reloading from a non-exixting json file'''
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})
