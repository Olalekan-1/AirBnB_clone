#!/usr/bin/python3
"""BaseModel Module

The BaseModel is a super class from which all other models
inherit from"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The super class from which other classes inherit
    """

    def __init__(self, *args, **kwargs):

        ignore = ["__class__"]  # attributes to ignore

        if len(kwargs.keys()) != 0:
            created_at = datetime.fromisoformat(kwargs["created_at"])
            updated_at = datetime.fromisoformat(kwargs["updated_at"])
            kwargs["updated_at"] = updated_at
            kwargs["created_at"] = created_at

            for key in [itm for itm in kwargs.keys() if itm not in ignore]:
                self.__setattr__(key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            storage.new(self)

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
        storage.save()

    def __str__(self):
        """Return String representation of object
        """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
