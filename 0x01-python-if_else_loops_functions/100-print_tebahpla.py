#!/usr/bin/python3

for x in range(0, 26):
    print(end=chr(~x % 2 * 32 + 64 + 26 - x).format())
