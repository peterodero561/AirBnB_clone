#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    '''Class BaseModel that defines all common
        attributes/methods for other class
    '''

    def __init__(self, *args, **kwargs):
        '''initializes the BaseModel object creeated'''
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.datetime.strptime
                    (value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        '''
        prints class name, class id, and dict when print function uses
        BaseModel class as argument
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates the public instance atrribute
        updated_at with the current datetime
        '''
        self.updated_at = datetime.datetime.now()

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
