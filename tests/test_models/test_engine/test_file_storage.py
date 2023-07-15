#!/usr/bin/python3
"""Test Module for FileStorage
"""

import os
import uuid
from unittest import TestCase
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(TestCase):
    """ Tests the functionality of FileStorage
    """
    @classmethod
    def setUpClass(cls):
        """Setup testing resources
        """
        file_path_key = "_FileStorage__file_path"
        cls.backup_file_path = "file_{}".format(
                str(uuid.uuid4()).replace('-', ""))
        cls.backed_up = False

        cls.file_path = FileStorage.__dict__[file_path_key]
        if os.path.exists(cls.file_path):
            os.rename(cls.file_path, cls.backup_file_path)
            cls.backed_up = True

    @classmethod
    def tearDownClass(cls):
        """ Release all used resources
        """

        if os.path.exists(cls.file_path):
            print("removing test file")
            os.remove(cls.file_path)
        if cls.backed_up:
            print("restoring storage file")
            os.rename(cls.backup_file_path, cls.file_path)

    def test_file_storage_attrubutes(self):
        """ Test attributes of the FileStorage

        The attributes tested are "__objects" that is
        represented by "_FileStorage__objects" and
        "__file_path" as "__FileStorage__file_path"
        """
        attributes = FileStorage.__dict__
        attr_1 = "_FileStorage__objects"
        self.assertIn(attr_1, attributes.keys())
        self.assertIsInstance(attributes[attr_1], dict)
        attr_2 = "_FileStorage__file_path"
        self.assertIn(attr_2, attributes.keys())
        self.assertIsInstance(attributes[attr_2], str)
        self.assertEqual(
                attributes[attr_2].split('.')[-1],
                "json"
                )

    def test_file_storage_init(self):
        """ Tests that FileStorage initialization

        This tests that FileStorage should be initialized
        without any argument
        """

        with self.assertRaises(TypeError):
            FileStorage(10)

    def test_file_storage_all(self):
        """Tests all method of FileStorage

        The all method must return dictionary and should
        not be called with any argument
        """
        storage = FileStorage()
        all_obj = storage.all()
        self.assertIsInstance(all_obj, dict)
        with self.assertRaises(Exception):
            storage.all(5)

    def test_file_storage_new(self):
        """Tests new method of FileStorage

        The new() adds an object to the FileStorage,
        it should be called with a single argument, which
        is an object that of BaseModel or its subclass
        """
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        objects = storage.all()
        self.assertTrue(objects)
        self.assertIn(
                "{}.{}".format(
                        type(model).__name__,
                        model.id), objects)

        with self.assertRaises(TypeError):
            storage.new()

    def test_storage_save_and_reload(self):
        """ Tests the save() and reload() methods

        The save() serializes and save all objects
        into a json file, the save recieves no arguments.
        The reload() loads the objects back to
        memory, it also receives no argument
        """
        storage_1 = FileStorage()
        storage_2 = FileStorage()
        model = BaseModel()
        storage_1.new(model)
        storage_1.save()

        storage_2.reload()
        all_data = storage_2.all()
        model_key = "{}.{}".format(
                    type(model).__name__,
                    model.id)
        self.assertIn(model_key, all_data)
        with self.assertRaises(TypeError):
            storage_2.save(model)
        with self.assertRaises(TypeError):
            storage_1.reload(5)
