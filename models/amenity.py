#!/usr/bin/python3
""" Defines the Amenity class.
    Inherits from BaseModel class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Represents the amenities of the Airbnb """

    name = ""

    def __init__(self, *args, **kwargs):
        """ initializes the Amenity class
        Arguments:
            args: Non keyworded arguments that can be passed
            kwargs: Keyworded arguments
        """
        super().__init__(*args, **kwargs)
