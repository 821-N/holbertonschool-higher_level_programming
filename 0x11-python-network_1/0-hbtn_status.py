#!/usr/bin/python3
"""
    0. What's my status? #0
"""


import urllib.request


with urllib.request.urlopen("https://intranet.hbtn.io/status") as res:
    data = res.read()
    print("Body response:")
    print("\t- type: " + str(type(data)))
    print("\t- content: " + str(data))
    print("\t- utf8 content: " + data.decode("utf-8"))
