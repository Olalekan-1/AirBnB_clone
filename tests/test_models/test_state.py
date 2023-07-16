#!/usr/bin/python3
"""Test Suite for State Model
"""

from unittest import TestCase
from models.base_model import BaseModel
from models.state import State


class TestStateModel(TestCase):
    """Tests State Model"""

    def test_state_is_subclass_of_base_model(self):
        """ Tests if State is a subclass of BaseModel
        """
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_name_is_string(self):
        """ Tests that name attribute of State is string
        """
        state = State()
        self.assertIsInstance(state.name, str)
        self.assertEqual(state.name, "")
