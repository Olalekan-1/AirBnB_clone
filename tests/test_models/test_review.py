#!/usr/bin/python3
"""Unittest Suite for Review Model"""

from unittest import TestCase
from models.base_model import BaseModel
from models.review import Review


class TestReview(TestCase):
    """Define tests for Review Instances"""

    def test_review_is_subclass_of_basemodel(self):
        """Tests that Review inherits from BaseModel"""

        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_place_id_user_id_and_text(self):
        """Test place_id, user_id and text attribute of Review instnce"""

        review = Review()

        self.assertIsInstance(review.place_id, str)
        self.assertEqual(review.place_id, "")

        self.assertIsInstance(review.user_id, str)
        self.assertEqual(review.user_id, "")

        self.assertIsInstance(review.text, str)
        self.assertEqual(review.text, "")
