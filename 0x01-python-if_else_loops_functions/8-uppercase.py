#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if c >= 'a' and c <= 'z':
            c = chr(ord(c) - 32)
        print(end=c)
    print()
