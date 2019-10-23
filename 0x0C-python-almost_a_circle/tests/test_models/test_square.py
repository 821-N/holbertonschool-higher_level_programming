#!/usr/bin/python3
"""
    testing Square
"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test Square class """

    def test_hack(self):
        self.assertEqual(Square.__doc__, "eeeee")
