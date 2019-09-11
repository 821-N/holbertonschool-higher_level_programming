#!/usr/bin/python3
for i in range(0, 99 + 1):
    if i // 10 < i % 10:
        print(end="{:02d}".format(i))
        print(end=", " if i < 89 else "\n")
