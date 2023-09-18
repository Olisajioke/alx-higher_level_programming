#!/usr/bin/python3
"""This module defines test cases for the Square class."""

import unittest
from models.square import Square


class TestSquareMethods(unittest.TestCase):

    def setUp(self):
        """Test the setup of the Square class."""
        self.square1 = Square(5, 1, 2, 42)
        self.square2 = Square(3, 0, 0, 10)

    def test_constructor(self):
        """Test the constructor of the Square class."""
        self.assertEqual(self.square1.size, 5)
        self.assertEqual(self.square1.x, 1)
        self.assertEqual(self.square1.y, 2)
        self.assertEqual(self.square1.id, 42)

        self.assertEqual(self.square2.size, 3)
        self.assertEqual(self.square2.x, 0)
        self.assertEqual(self.square2.y, 0)
        self.assertEqual(self.square2.id, 10)

    def test_area(self):
        """Test the area() method of the Square class."""
        self.assertEqual(self.square1.area(), 25)
        self.assertEqual(self.square2.area(), 9)

    def test_display(self):
        """Test the display() method of the Square class."""
        expected_output1 = "\n\n #####\n #####\n #####\n #####\n #####\n"
        expected_output2 = "###\n###\n###\n"
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.square1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output1)

        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.square2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output2)

    def test_str(self):
        """Test the __str__() method of the Square class."""
        self.assertEqual(str(self.square1), "[Square] (42) 1/2 - 5")
        self.assertEqual(str(self.square2), "[Square] (10) 0/0 - 3")

    def test_update(self):
        """Test the update of the Square class."""
        self.square1.update(10, 30, 20, 3)
        self.assertEqual(str(self.square1), "[Square] (20) 10/30 - 3")

    def test_to_dictionary(self):
        """Test the to_dictionary() method of the Square class."""
        expected_dict1 = {'id': 42, 'x': 1, 'size': 5, 'y': 2}
        expected_dict2 = {'id': 10, 'x': 0, 'size': 3, 'y': 0}
        self.assertEqual(self.square1.to_dictionary(), expected_dict1)
        self.assertEqual(self.square2.to_dictionary(), expected_dict2)

    def test_invalid_size(self):
        """Test setting an invalid size value."""
        with self.assertRaises(ValueError):
            self.square1.size = 0

    def test_invalid_x(self):
        """Test setting an invalid x value."""
        with self.assertRaises(ValueError):
            self.square1.x = -1

if __name__ == '__main__':
    unittest.main()
