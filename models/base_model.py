#!/usr/bin/python3
import uuid
import datetime

"""Defines all common attributes/methods for other classes."""


class BaseModel():
    """Represents a model
    Attributes:
        id (str): unique ID for each instance.
        created_at (datetime): Current datetime an instance was created.
        updated_at (datetime): Current datetime an instance was updated.
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Returns printable representation of the model"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attributes <updated_at>
        with current date and time
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all key/value of __dict__
        of the instance
        """
        attr_dict = self.__dict__.copy()
        attr_dict['__class__'] = self.__class__.__name__
        attr_dict['created_at'] = self.created_at.isoformat()
        attr_dict['updated_at'] = self.updated_at.isoformat()

        return attr_dict
