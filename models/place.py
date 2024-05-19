#!/usr/bin/python3
""" Defines the Place class.
    Inherits from BaseModel class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Represents the place where the Airbnb at """

    def __init__(self, *args, **kwargs):
        """ initializes the Place class
        Arguments:
            args: Non keyworded arguments that can be passed
            kwargs: Keyworded arguments
        """
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__(*args, **kwargs)
