#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, MetaData, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

#|---------------------------- Class Attributes ----------------------------|

    __tablename__ = 'cities'
    name = Column(String(128), nulleable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
