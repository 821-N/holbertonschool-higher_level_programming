#!/usr/bin/python3
"""
    8. Create object from a JSON file
"""


from json import loads


def load_from_json_file(filename):
    with open(filename) as f:
        return loads(f.read())
