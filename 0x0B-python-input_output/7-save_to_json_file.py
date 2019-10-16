#!/usr/bin/python3
"""
    7. Save Object to a file
"""


from json import dumps


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        f.write(dumps(my_obj))
