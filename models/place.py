#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, ForeignKey, Float, Integer, Table
from sqlalchemy.orm import relationship
import os
import models

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id",
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id",
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship('Amenity',
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """ get the reviews in FileStorage """
            all_reviews = []
            for obj in models.storage.all(Review).values():
                if obj.place_id == self.id:
                    all_reviews.append(obj)
            return all_reviews

        @property
        def amenities(self):
            """ get the amenity in FileStorage """
            all_ameny = []
            for obj in models.storage.all(Amenity).values():
                if obj.place_id == self.id:
                    all_ameny.append(obj)
            return all_ameny

        @amenities.setter
        def amenities(self, obj):
            """ set the amenity in FileStorage """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
