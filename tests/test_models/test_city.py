#!/usr/bin/python3
""" Test Module for City Model
"""
from unittest import TestCase
from models.base_model import BaseModel
from models.city import City


class TestCityModel(TestCase):
    """Define Tests for the City Model
    """

    def test_city_subclass_of_base_model(self):
        """Test that city is a subclass of BaseModel
        """
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_name_and_state_id(self):
        """ Test city.state_id
        """
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertEqual(city.state_id, "")
        self.assertIsInstance(city.name, str)
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
