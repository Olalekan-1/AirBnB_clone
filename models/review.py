#!/usr/bin/python3
"""This is the Module for Review Class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents Review Model"""

    place_id = ""
    user_id = ""
    text = ""
