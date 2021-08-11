#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    
#|---------------------------- Class Attributes ----------------------------|

    id = Column(string(60), primary_key=True, nulleable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nulleable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nulleable=False)

    
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
                  
        time = datetime.now()
        self.id = str(uuid4())
        self.created_at = time
        self.updated_at = time

        if kwargs:
            for key in kwargs.keys():
                if key == "created_at":
                    time = datetime.strptime(
                        kwargs.get(key),
                        "%Y-%m-%dT%H:%M:%S.%f")
                    self.created_at = time
                elif key == "updated_at":
                    time = datetime.strptime(
                        kwargs.get(key),
                        "%Y-%m-%dT%H:%M:%S.%f")
                    self.updated_at = time
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        
        if "_sa_instance_state" in dictionary:
            dictionary.pop("_sa_instance_state", None)
        
        return dictionary

    def delete(self):
        """ delete the current instance from the storage """
        
        storage.delete(self)
