#!/usr/bin/python3
""" Place Module for HBNB project """

from sqlalchemy.sql.schema import ColumnDefault
from sqlalchemy.sql.sqltypes import Float, Integer
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__="places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False,)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False,)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, ColumnDefault(0), nullable=False)
    number_bathrooms = Column(Integer, ColumnDefault(0), nullable=False)
    max_guest = Column(Integer, ColumnDefault(0), nullable=False)
    price_by_night = Column(Integer, ColumnDefault(0), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
