#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    @property
    def objects(self):
        """
            Getter for objects
        """

        return (self.__objects)

    def close(self):
        self.reload()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            cls_dict = {}
            for key, value in self.__objects.items():
                if value.__class__ == cls:
                    cls_dict[key] = value
            return cls_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """ Delete object from JSON database """
        if obj:
            obj_id = obj.__dict__['id']
            for key in self.__objects:
                id = key.split('.')
                id = id[1]
                if obj_id == id:
                    self.__objects.pop(key)
                    self.save()
                    break
        else:
            pass

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
