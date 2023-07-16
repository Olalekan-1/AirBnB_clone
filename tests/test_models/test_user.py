#!/usr/bin/python3
""" Unittest Suite for User Model
"""

from unittest import TestCase
from models.user import User
from models.base_model import BaseModel


class TestUserModel(TestCase):
    """Define tests for the User Class"""

    def test_user_is_subclass_of_base_model(self):
        """Tests that User Inherits from BaseModel"""

        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_email_password_and_names(self):
        """Define tests for user's details

        The detials are email, password, first_name and last_name
        """
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertEqual(user.email, "")

        self.assertIsInstance(user.password, str)
        self.assertEqual(user.password, "")

        self.assertIsInstance(user.first_name, str)
        self.assertEqual(user.first_name, "")

        self.assertIsInstance(user.last_name, str)
        self.assertEqual(user.last_name, "")
