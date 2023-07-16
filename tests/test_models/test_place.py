#!/usr/bin/python3
"""Unittest Module for Place model
"""

from unittest import TestCase
from models.base_model import BaseModel
from models.place import Place


class TestCityModel(TestCase):
    """Define Tests for City Model"""

    def test_place_is_subclass_of_basemodel(self):
        """Test that Place inherits from BaseModel
        """

        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_city_id_and_user_id(self):
        """Tests the city_id and user_id of Place model"""

        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertEqual(place.city_id, "")

        self.assertIsInstance(place.user_id, str)
        self.assertEqual(place.user_id, "")

    def test_name_and_description(self):
        """ Tests the name and description of Place model """

        place = Place()
        self.assertIsInstance(place.name, str)
        self.assertEqual(place.name, "")

        self.assertIsInstance(place.description, str)
        self.assertEqual(place.description, "")

    def test_number_rooms_and_bathrooms(self):
        """ Test the rooms and bathrooms number
        """

        place = Place()
        self.assertIsInstance(place.number_rooms, int)
        self.assertEqual(place.number_rooms, 0)

        self.assertIsInstance(place.number_bathrooms, int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_price_by_night(self):
        """ Test the max_guest and price_by_night of Place"""

        place = Place()
        self.assertIsInstance(place.max_guest, int)
        self.assertEqual(place.max_guest, 0)

        self.assertIsInstance(place.price_by_night, int)
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_and_longitude(self):
        """Tests latitude and longitude of Place intancee"""

        place = Place()
        self.assertIsInstance(place.latitude, float)
        self.assertEqual(place.latitude, 0.0)

        self.assertIsInstance(place.longitude, float)
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids(self):
        """Tests the amenity_ids of Place model"""

        place = Place()
        self.assertIsInstance(place.amenity_ids, list)
        self.assertEqual(len(place.amenity_ids), 0)
