#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ Database Storage """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor of the database """
