#!/usr/bin/env python3
""" This module contains a user class that inherite
attributes from BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ A user class that holds the personal
    details of a user
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
