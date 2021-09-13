#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel
from models import storage
from models.city import City


class State(BaseModel):
    """ State class """

    @property
    def cities(self):
        all_cities = storage.all(City)
        city_list = []
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)

        return city_list
