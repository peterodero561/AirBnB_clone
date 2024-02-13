#!/usr/bin/python3
'''Module for the FileStorage classs'''
import json


class EmptyFileError(Exception):
    """Custom exception for empty file."""
    pass


class FileStorage:
    '''class FileStorage that serializes instances to a
        JSON file and deserializes JSON file to instances
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''method to return the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''Set in __objects the onj with key <obj class name>.id'''
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the json file'''
        if not self.__objects:
            raise EmptyFileError("No objects to save.")
        else:
            serialized_objs = {}
            for key, obj in self.__objects.items():
                serialized_objs[key] = obj.to_dict()
            with open(self.__file_path, 'w', encoding="utf-8") as f:
                json.dump(serialized_objs, f)

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)'''
        from ..base_model import BaseModel
        from ..user import User
        from ..place import Place
        from ..state import State
        from ..city import city
        from ..amenity import Amenity
        from ..review import Review
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    obj = cls(**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            self.__objects = {}
