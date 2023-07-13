#!/usr/bin/python3
"""BaseModel Module

The BaseModel is a super class from which all other models
inherit from"""

import uuid
from datetime import datetime


class BaseModel:
    """The super class from which other classes inherit
    """
    def __init__(self):
        """ Instance of BaseModel created"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def to_dict(self):
        """Return a dictionary of instance attributes

        the dictionary is a key/value pair of attribute name/value
        include a key "__class__" with a value of instance class name
        """
        model_dict = {'__class__': type(self).__name__}
        for key, value in self.__dict__.items():
            model_dict[key] = value
        model_dict['created_at'] = model_dict['created_at'].isoformat()
        model_dict['updated_at'] = model_dict['updated_at'].isoformat()
        return model_dict

    def save(self):
        """Set updated_at attribute to current datetime
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """Return String representation of object
        """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
