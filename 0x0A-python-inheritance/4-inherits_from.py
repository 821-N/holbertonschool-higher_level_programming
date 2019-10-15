#!/usr/bin/python3
"""
    4. Only sub class of
"""


def inherits_from(obj, a_class):
    """ you get the idea """
    return type(obj) is not a_class and isinstance(obj, a_class)
