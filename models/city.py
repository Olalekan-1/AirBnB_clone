#!/usr/bin/python3
""" This module Define the City Model
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Define the City Model
    """

    def __init__(self, state_id="", *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.state_id = state_id
        self.name = ""
