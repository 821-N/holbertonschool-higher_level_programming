#!/usr/bin/python3
"""
    9. Load, add, save
"""


from sys import argv


n = "add_item.json"
try:
    items = __import__('8-load_from_json_file').load_from_json_file(n)
except:
    items = []
finally:
    __import__('7-save_to_json_file').save_to_json_file(items + argv[1:], n)
