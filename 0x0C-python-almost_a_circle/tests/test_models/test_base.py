#!/usr/bin/python3
"""This module defines test cases for the Base class."""
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):

    def setUp(self):
        """Set up common parameters for testing."""
        self.obj1 = Base()
        self.obj2 = Base(10)

    def test_constructor(self):
        """Test the constructor of the Base class."""
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 10)

    def test_to_json_string(self):
        """Test the to_json_string() method of the Base class."""
        dict_list = [{'id': 1, 'key': 'value'}, {'id': 2, 'key': 'value'}]
        json_string = Base.to_json_string(dict_list)
        expected_json = '[{"id": 1, "key": "value"}, {"id": 2, "key": "value"}]'
        self.assertEqual(json_string, expected_json)

    def test_from_json_string(self):
        """Test the from_json_string() method of the Base class."""
        json_string = '[{"id": 1, "key": "value"}, {"id": 2, "key": "value"}]'
        dict_list = Base.from_json_string(json_string)
        expected_dict_list = [{'id': 1, 'key': 'value'}, {'id': 2, 'key': 'value'}]
        self.assertEqual(dict_list, expected_dict_list)

    def test_create_invalid_class(self):
        """Test create() with an unsupported class."""
        with self.assertRaises(ValueError):
            data = {'id': 1, 'size': 3}
            obj = Base.create(**data)


if __name__ == '__main__':
    unittest.main()

