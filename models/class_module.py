#!/usr/bin/python3
""" imports all classes """
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City

# baseModel = BaseModel()
# user = User()
# amenity = Amenity()
# review = Review()
# state = State()
# place = Place()
# city = City()
#
#
# def get_all_class():
#     """ Return dictionary of all classes """
#
#     all_class = {
#         f"BaseModel.{baseModel.id}": baseModel,
#         f"User.{user.id}": user.to_dict(),
#         f"Amenity.{amenity.id}": amenity.to_dict(),
#         f"Review.{review.id}": review.to_dict(),
#         f"State.{state.id}": state.to_dict(),
#         f"Place.{place.id}": place.to_dict(),
#         f"City.{city.id}": city.to_dict()
#     }
#
#     return all_class
