#!/usr/bin/python3
""" Contains the TestDBStorageDocs and TestDBStorage classes """

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get(self):
        """Test that get returns the correct object"""
        state = State(name="California")
        state.save()
        self.assertEqual(state, models.storage.get(State, state.id))



import pytest

class TestGet:

    # should retrieve an object of a given class with a valid id
    def test_retrieve_object_with_valid_id(self):
        # Initialize DBStorage object
        db_storage = DBStorage()

        # Create a mock session object
        mock_session = mocker.Mock()
        db_storage._DBStorage__session = mock_session

        # Create a mock class object
        mock_class = mocker.Mock()

        # Call the get method with a valid id
        result = db_storage.get(mock_class, 1)

        # Assert that the query method was called with the correct arguments
        mock_session.query.assert_called_once_with(mock_class)

        # Assert that the filter_by method was called with the correct arguments
        mock_session.query.return_value.filter_by.assert_called_once_with(id=1)

        # Assert that the first method was called
        mock_session.query.return_value.filter_by.return_value.first.assert_called_once()

        # Assert that the result is the return value of the first method
        assert result == mock_session.query.return_value.filter_by.return_value.first.return_value

    # should handle invalid id types (e.g. string instead of integer)
    def test_handle_invalid_id_types(self):
        # Initialize DBStorage object
        db_storage = DBStorage()

        # Create a mock session object
        mock_session = mocker.Mock()
        db_storage._DBStorage__session = mock_session

        # Create a mock class object
        mock_class = mocker.Mock()

        # Call the get method with an invalid id type
        result = db_storage.get(mock_class, "invalid_id")

        # Assert that the query method was not called
        mock_session.query.assert_not_called()

        # Assert that the result is None
        assert result is None

class test_count(unittest.TestCase):
    """Test the count method of the DBStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count(self):
        """Test that count returns the number of objects in storage"""
        count = models.storage.count()
        self.assertEqual(type(count), int)
        state = State(name="California")
        state.save()
        count = models.storage.count()
        self.assertEqual(count, 1)

    

import pytest

class TestCount:

    # Should return 0 when there are no objects in storage
    def test_return_zero_when_no_objects(self):
        db_storage = DBStorage()
        assert db_storage.count() == 0

    # Should raise an error when cls is not a class
    def test_raise_error_when_cls_not_class(self):
        db_storage = DBStorage()
        with pytest.raises(TypeError):
            db_storage.count("not_a_class")
