#!/usr/bin/python3

""" These are functions that power the console class under the hood """


from models.class_module import BaseModel, User, Place, State, Review, City


def create_object(class_name):
    """ creates an object of class_name """
    if class_name:
        if class_name == "BaseModel":
            return BaseModel()
        elif class_name == "User":
            return User()
        elif class_name == "Place":
            return Place()
        elif class_name == "State":
            return State()
        elif class_name == "Review":
            return Review()
        elif class_name == "City":
            return City()
    else:
        return None


def check_class_name(classname, all_object):
    """ Returns True if class name exist in the list """
    if classname and all_object:
        for key, value in all_object.items():
            if key.startswith(f"{classname}."):
                return True

        return False


        # def get_available_classes():
        #     """ Returns a dictionary of available classes """
        #
CLASSES = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "Review": Review,
    "City": City,
}
