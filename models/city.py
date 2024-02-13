#!/usr/bin/python3

import json
from models.base_model import BaseModel


class City(BaseModel):
    '''Class City inheriting from BaseModel'''
    state_id = ""
    name = ""

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
