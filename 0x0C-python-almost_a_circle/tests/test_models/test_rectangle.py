#!/usr/bin/python3
"""This module defines test cases for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):

    def setUp(self):
        """Initialize some common parameters for testing"""
        self.rect = Rectangle(5, 4, 1, 2, 42)

    def test_constructor(self):
        """Test the constructor of the Rectangle class."""
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.height, 4)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 2)
        self.assertEqual(self.rect.id, 42)

    def test_area(self):
        """Test the area() method of the Rectangle class."""
        self.assertEqual(self.rect.area(), 20)

    def test_display(self):
        """Test the display() method of the Rectangle class."""
        expected_output = "\n\n #####\n #####\n #####\n #####\n"
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        """Test the __str__() method of the Rectangle class."""
        self.assertEqual(str(self.rect), "[Rectangle] (42) 1/2 - 5/4")

    def test_update(self):
        self.rect.update(10, 20, 3, 30, 40)
        self.assertEqual(str(self.rect), "[Rectangle] (3) 10/20 - 40/30")

    def test_to_dictionary(self):
        """Test the to_dictionary() method of the Rectangle class."""
        expected_dict = {'x': 1, 'width': 5, 'id': 42, 'height': 4, 'y': 2}
        self.assertEqual(self.rect.to_dictionary(), expected_dict)

    def test_invalid_width(self):
        """Test setting an invalid width value."""
        with self.assertRaises(ValueError):
            self.rect.width = 0

    def test_invalid_x(self):
        """Test setting an invalid x value."""
        with self.assertRaises(ValueError):
            self.rect.x = -1

if __name__ == '__main__':
    unittest.main()
