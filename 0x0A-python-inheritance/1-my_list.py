#!/usr/bin/python3
"""
    MyList
"""


class MyList(list):
    """ Custom list class """

    def print_sorted(self):
        """ print a sorted list """
        print(sorted(self))
