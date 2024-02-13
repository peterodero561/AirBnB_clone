#!/usr/bin/python3
import uuid
import json
import datetime


class BaseModel:
    '''Class BaseModel that defines all common
        attributes/methods for other class
    '''

    def __init__(self, *args, **kwargs):
        '''initializes the BaseModel object creeated'''
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at'] and \
                        isinstance(value, str):
                    value = datetime.datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            # Add a call to the new() method on storage
            storage.new(self)

    def __str__(self):
        '''
        prints class name, class id, and dict when print function uses
        BaseModel class as argument
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates the public instance atrribute
        updated_at with the current datetime and
        Saves instance to storage
        '''
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        '''returns a dictionary containing all
        keys/values of __dict__ of the instance:
        '''
        created_at_ISO = self.created_at.isoformat()
        updated_at_ISO = self.updated_at.isoformat()
        dictionary = {
                **self.__dict__,
                '__class__': self.__class__.__name__,
                'created_at': created_at_ISO,
                'updated_at': updated_at_ISO
                }
        return dictionary

    @classmethod
    def from_dict(cls, dict_obj):
        '''creates an instance from a dictionary'''
        if '__class__' in dict_obj:
            class_name = dict_obj.pop('__class__')
            if class_name == cls.__name__:
                for key, value in dict_obj.items():
                    if key in ('created_at', 'updated_at'):
                        if isinstance(value, str):
                            value = datetime.datetime.strptime(
                                    value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(cls, key, value)
                        # dict_obj[key] = value
                return cls(**dict_obj)
        return None

    @classmethod
    def load(cls, class_name, instance_id):
        """Load an object from JSON file based on class name and instance id"""
        try:
            with open("file.json", 'r') as file:
                data = json.load(file)
                key = f"{class_name}.{instance_id}"
                if key not in data:
                    print("** no instance **")
                    return {}
                obj_data = data[key]
                if obj_data["__class__"] != class_name:
                    print("** no instance found **")
                    return {}
                obj = cls(**obj_data)
                return obj
        except FileNotFoundError:
            pass
        raise FileNotFoundError("Instance not found in JSON file")
