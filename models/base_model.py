#!/usr/bin/python3
'''BaseModel class module'''
import datetime
import uuid
import models


class BaseModel:
    '''defines all common attributes/methods for other classes'''
    def __init__(self, *args, **kwargs):
        '''initialization'''
        if kwargs != {}:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == 'created_at':
                    self.created_at = datetime.datetime.fromisoformat(value)
                if key == 'updated_at':
                    self.updated_at = datetime.datetime.fromisoformat(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''defines how the should be represented as a string'''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''updates the attribute updated_at with the current datetime'''
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of the instance'''
        res = self.__dict__.copy()
        res['created_at'] = res['created_at'].isoformat()
        res['updated_at'] = res['updated_at'].isoformat()
        res['__class__'] = self.__class__.__name__
        return res
