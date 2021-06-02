#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="all, delete",
                              backref="state")
    else:
        @property
        def cities(self):
            """List of City instances with state_id equals"""
            city_list = []
            all_cities = models.storage.all(City)
            for obj in all_cities.values():
                if obj.state_id == self.id:
                    city_list.append(obj)
            return city_list
