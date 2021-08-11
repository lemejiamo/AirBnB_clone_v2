#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

#|---------------------------- Class Attributes ----------------------------|

    __tablename__ = 'cities'
    name = Column(string(128), nulleable=False)
    state_id = Column(string(60), ForeignKey("states.id"), nullable=False)
