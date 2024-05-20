#!/usr/bin/python3
""" Defines the review class.
    Inherits from BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Represents the Review of the Airbnb """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ initializes the Review class
        Arguments:
            args: Non keyworded arguments that can be passed
            kwargs: Keyworded arguments
        """
        super().__init__(*args, **kwargs)
