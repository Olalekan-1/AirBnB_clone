#!/usr/bin/python3
"""This is the Module for Review Class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents Review Model"""

    def __init__(self, place_id="", user_id="", *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = ""
