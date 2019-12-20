#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.review import Review
from models.place import Place


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """

    review = relationship("Review", backref="user",
                          cascade="all, delete, delete-orphan")
    places = relationship("Place", backref="user",
                          cascade="all, delete, delete-orphan")
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    password = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    __tablename__ = 'users'
