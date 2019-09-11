#!/usr/bin/python3
for i in range(0, 99 + 1):
    print(end="{:02d}".format(i))
    print(end=", " if i < 99 else "\n")
