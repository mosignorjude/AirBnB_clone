#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines the Amenity class.
    Inherits from BaseModel class
"""


class Amenity(BaseModel):
    """ Represents the amenities of the Airbnb """

    def __init__(self, *args, **kwargs):
        """ initializes the Amenity class
        Arguments:
            args: Non keyworded arguments that can be passed
            kwargs: Keyworded arguments
        """
        self.name = ""
        super().__init__(*args, **kwargs)
