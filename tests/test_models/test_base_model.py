#!/usr/bin/env python3

"""This module provides test suit for
AirBnB project.
"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class Testbase(unittest.TestCase):

    """ TestCases to test the base instance
    """

    def setUp(self):
        """ Test the set up"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def test_instance_id(self):
        """ Test the instance id """
        base_id = self.base1.id
        self.assertNotEqual(base_id, self.base2.id)
        self.assertEqual(self.base1.id, base_id)
        self.assertIsInstance(self.base1.id, str)
        self.assertTrue(hasattr(self.base2, "id"))
        self.assertIs(type(self.base2.id), str)

    def test_created_at(self):
        """ Test the created at attribute """
        # formatted = self.base1.created_at
        self.assertTrue(hasattr(self.base2, "created_at"))
        self.assertIs(type(self.base2.created_at), datetime)
        self.base1.name = "olalekan"
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)
        self.assertLess(self.base1.created_at, self.base1.updated_at)

    def test_updated_at(self):
        """ Test the updated_at attribute """
        self.assertTrue(hasattr(self.base1, "updated_at"))
        self.assertIs(type(self.base1.updated_at), datetime)
        self.base2.name = "Idris"
        self.assertGreater(self.base2.updated_at, self.base2.created_at)

    def test_to_dict(self):
        """ Test the to dict attribute """
        b = self.base2.to_dict()
        formatted = self.base2.created_at.isoformat()
        formatted2 = self.base2.updated_at.isoformat()
        self.assertTrue(hasattr(self.base1, "to_dict"))
        self.assertEqual(self.base2.to_dict(), b)

        self.assertEqual(b['created_at'], formatted)
        self.assertEqual(b['updated_at'], formatted2)
        self.assertTrue('__class__' in b)
        self.assertEqual(b['__class__'], self.base1.__class__.__name__)
        self.assertEqual(b['__class__'], 'BaseModel')

    def test_save(self):
        """ Test the save update attribute """
        self.assertTrue(hasattr(self.base1, "save"))
        self.base1.age = 10
        # time = self.base1.save()
        # self.assertEqual(time, self.base1.save())

    def test__str__(self):
        """ Test the string representaion """
        self.assertTrue(hasattr(self.base1, "__str__"))
        b = "[{}] ({}) {}".format(self.base2.__class__.__name__, self.base2.id,
                                  self.base2.__dict__)
        self.assertEqual(str(self.base2), b)


if __name__ == '__main__':
    unittest.main()
