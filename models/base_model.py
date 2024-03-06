#!/usr/bin/python3
"""
a class BaseModel that defines all common
attributes/methods for other classes
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """ base class for managing common attributes and methods
        for derived classes """
    def __init__(self, *args, **kwargs):
        """ create an instance with dictionary representation without class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            frmt_time = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(value, frmt_time))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """ Return a string representation of the object """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the 'updated_at' timestamp to the current date and time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary representation of the object """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dicti
