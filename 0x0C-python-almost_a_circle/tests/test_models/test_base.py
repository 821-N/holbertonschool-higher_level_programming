#!/usr/bin/python3
"""
    testing Base
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Base class """

    def test_hack(self):
        self.assertEqual(Base.__doc__, "eeeee")
