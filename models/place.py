#!/usr/bin/python3
""" Defines the Place class.
    Inherits from BaseModel class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Represents the place where the Airbnb at """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ initializes the Place class
        Arguments:
            args: Non keyworded arguments that can be passed
            kwargs: Keyworded arguments
        """
        super().__init__(*args, **kwargs)
