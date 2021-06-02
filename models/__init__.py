#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

database = os.getenv('HBNB_TYPE_STORAGE')
if database == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
