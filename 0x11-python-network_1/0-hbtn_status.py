#!/usr/bin/python3
"""
    0. What's my status? #0
"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as res:
        data = res.read()
        print("Body response:")
        print("    - type: " + str(type(data)))
        print("    - content: " + str(data))
        print("    - utf8 content: " + data.decode("utf-8"))
