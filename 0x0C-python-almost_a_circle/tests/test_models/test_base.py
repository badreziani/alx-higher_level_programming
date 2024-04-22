#!/usr/bin/python3
"""
test_base module

This module contains tests for the Base class
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """class TestBase.
    Test all parts of the Base class
    """
    def test_id(self):
        b1 = Base()
        self.assertIsInstance(b1.id, int)
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(50)
        self.assertEqual(b3.id, 50)

        b4 = Base()
        self.assertEqual(b4.id, 3)

        b5 = Base(None)
        self.assertEqual(b5.id, 4)
