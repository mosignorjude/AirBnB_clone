#!/usr/bin/python3
""" Defines the State class.
    Inherits from BaseModel class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Represents the state of the Airbnb """

    def __init__(self, *args, **kwargs):
        """ initializes the state class
        Arguments:
            args: Non keyworded arguments that can be passed
            kwargs: Keyworded arguments
        """
        self.name = ""
        super().__init__(*args, **kwargs)
