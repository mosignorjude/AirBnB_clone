#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines the review class.
    Inherits from BaseModel class
"""


class Review(BaseModel):
    """ Represents the Review of the Airbnb """

    def __init__(self, *args, **kwargs):
        """ initializes the Review class
        Arguments:
            args: Non keyworded arguments that can be passed
            kwargs: Keyworded arguments
        """
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
