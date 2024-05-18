#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines the City class.
    Inherits from BaseModel class
"""


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
