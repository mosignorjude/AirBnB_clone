#!/usr/bin/python3
""" Defines a user that inherits from class BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Represents a user from base model """

    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
