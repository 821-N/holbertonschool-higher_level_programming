#!/usr/bin/python3
"""
    testing Rectangle
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test Rectangle class """

    def test_hack(self):
        self.assertEqual(Rectangle.__doc__, "eeeee")
