#!/usr/bin/python3
"""
    testing Rectangle
"""


import unittest
from models.rectangle import Rectangle
import random

class TestRectangle(unittest.TestCase):
    """ Test Rectangle class """

    def test_init(self):
        a = Rectangle(1, 5)
        q = a.to_dictionary()
        del q["id"]
        self.assertEqual(q, {"x": 0, "y": 0, "width": 1, "height": 5})
        with self.assertRaises(ValueError):
            a.width = -1;
        with self.assertRaises(TypeError):
            a.height = "aaa";
        with self.assertRaises(TypeError):
            a.x = 0.1
        with self.assertRaises(TypeError):
            a.y = None
        a.width=17
        a.height=65
        a.x=6
        a.y=10
        self.assertEqual(a.width, 17)
        self.assertEqual(a.height, 65)
        self.assertEqual(a.x, 6)
        self.assertEqual(a.y, 10)

    def test_str(self):
        self.assertEqual(str(Rectangle(1, 9, 15, 0, 6)), "[Rectangle] (6) 15/0 - 1/9")
