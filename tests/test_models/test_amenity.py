#!/usr/bin/python3
""" Unittest Module for Amenity Model
"""

from unittest import TestCase
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityModel(TestCase):
    """Define the tests for Amenity Model"""

    def test_amenity_subclass_of_base_model(self):
        """Test that Amenity inherits from BaseModel
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_name(self):
        """Test the amenity name"""

        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
        self.assertEqual(amenity.name, "")
