#!/usr/bin/python3
"""contains dbstorage class"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """  """
    __engine = None
    __session = None

    def __init__(self):
        """ create instances of the initial method
         """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        # dialect+driver://username:password@host:port/database
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:/{}".
             format(user, password, host,db), pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ this method must return a dictionary """


    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """  commit all changes  """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj is not None:
            self.__session.dlete(obj)

    def reload(self):
        """  """
