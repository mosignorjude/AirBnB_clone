#!/usr/bin/python3
""" Defines the City class.
    Inherits from BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Represents the City of the Airbnb """

    def __init__(self, *args, **kwargs):
        """ initializes the City class
        Arguments:
            args: Non keyworded arguments that can be passed
            kwargs: Keyworded arguments
        """
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
