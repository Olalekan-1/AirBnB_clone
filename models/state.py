#!/usr/bin/python3
""" State Model Module
"""

from models.base_model import BaseModel


class State(BaseModel):
    """ Define State Model"""

    def __init__(self):
        super().__init__(self)
        self.name = ""
