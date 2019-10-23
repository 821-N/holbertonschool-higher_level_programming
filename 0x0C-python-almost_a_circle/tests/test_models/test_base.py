#!/usr/bin/python3
"""
    testing Base
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Base class """

    def test_init(self):
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base(5)
        self.assertEqual(b.id, 5)
        c = Base()
        self.assertEqual(c.id, 2)

    def test_json(self):
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.to_json_string(None), "[]")
        test = [{"id":12},{"id":13}]
        s = Base.to_json_string(test)
        self.assertEqual(Base.from_json_string(s), test)
