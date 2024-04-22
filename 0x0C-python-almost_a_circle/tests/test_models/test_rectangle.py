#!/usr/bin/python3
"""
test_rectangle module

This module contains tests for the Rectangle class
"""
import unittest


class TestRectangle(unittest.TestCase):
    """class TestRectangle.
    Test all parts of the Rectangle class
    """

    @classmethod
    def setUpClass(cls):
        """Creates Rectangle instances
        that will be used to test the class
        """
        cls.r1 = Rectangle(2, 6)
        cls.r2 = Rectangle(3, 7)
        cls.r3 = Rectangle(10, 2, 0, 0, 50)
        cls.r4 = Rectangle(7, 5)
        cls.r5 = Rectangle(10, 2, 3, 5, None)

    def test_id():
        """Tests for id."""
        self.assertIsInstance(r1.id, int)
        self.assertEqual(cls.r1.id, 1)
        self.assertEqual(cls.r2.id, 2)
        self.assertEqual(cls.r3.id, 50)
        self.assertEqual(cls.r4.id, 3)
        self.assertEqual(cls.r5.id, 4)

    def test_width(self):
        self.assertIsInstance(cls.r1.width, int)
        self.assertEqual(cls.r1.width, 2)
        cls.r1.width = 5
        self.assertEqual(cls.r1.width, 5)
        with assertRaises(ValueError, msg="width must be > 0"):
            cls.r1.width = -6
        with assertRaises(TypeError, msg="width must be an integer"):
            cls.r1.width = "5"

    def test_height(self):
        pass

    def test_x(self):
        pass

    def test_y(self):
        pass
