#!/usr/bin/python3
"""
test_base module

This module contains tests for the Base class
"""
import unittest
from models import base

class TestBase(unittest.TestCase):
    """class TestBase.
    Test all parts of the Base class
    """

    def test_int(self):
        self.b = base.Base("")
        self.assertIsInstance(self.b.id, int)


if __name__ == "__main__":
    unittest.main()
