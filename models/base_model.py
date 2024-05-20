#!/usr/bin/python3
""" Defines the Base Model of the Airbnb project.
    Other classes inherits from this Class.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Represents Airbnb model
    Attributes:
        id (str): unique ID for each instance.
        created_at (datetime): Current datetime an instance was created.
        updated_at (datetime): Current datetime an instance was updated.
    """

    def __init__(self, *args, **kwargs):
        """class constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        parsed_time = datetime.utcnow.fromisoformat(value)
                        setattr(self, key, parsed_time)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """ Returns printable representation of the model"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attributes <updated_at>
        with current date and time
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all key/value of __dict__
        of the instance
        """
        attr_dict = self.__dict__.copy()
        attr_dict['__class__'] = self.__class__.__name__
        attr_dict['created_at'] = self.created_at.isoformat()
        attr_dict['updated_at'] = self.updated_at.isoformat()

        return attr_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """ Creates an instance from a dictionary """
        return cls(**obj_dict)
