#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import environ
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    name = Column(String(128), nullable=False)
    __tablename__ = 'states'

    if 'HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', cascade="all, delete-orphan",
                              backref="state")
    else:
        @property
        def cities(self):
            stat = self.id
            lis = []

            for k, v in models.storage.all().items():
                if "City" in k and v.state_id == self.id:
                    lis.append(v)

            return lis
