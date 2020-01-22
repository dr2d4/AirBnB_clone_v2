#!/usr/bin/python3
"""This is the db storage class for AirBnB"""

from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from models.city import City
from os import getenv


class DBStorage:
    """ Database Storage """
    __session = None
    __engine = None

    def __init__(self):
        """ Constructor of the database """
        config_db = 'mysql+mysqldb://{}:{}@{}:3306/{}'
        password = getenv('HBNB_MYSQL_PWD')
        database = getenv('HBNB_MYSQL_DB')
        user = getenv('HBNB_MYSQL_USER')
        host = getenv('HBNB_MYSQL_HOST')
        hbnb_env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            config_db.format(user, password, host, database),
            pool_pre_ping=True)

        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ return all objects of one or more tables """
        objs = {}

        if cls:
            cls.remove('BaseModel')

        for table in cls:
            for obj in self.__session.query(eval(table)).all():
                key = obj.__class__.__name__ + '.' + obj.id
                objs[key] = obj

        return objs

    def new(self, obj):
        """ add a new object """
        self.__session.add(obj)

    def save(self):
        """ save all changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete object """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload all objects """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(session)
        self.__session = session()

    def close(self):
        """ close session """
        self.__session.close()
