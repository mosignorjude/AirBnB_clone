#!/usr/bin/python3
""" Defines a user that inherits from class BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Represents a user from base model """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Class constructor """
        super().__init__(*args, **kwargs)
