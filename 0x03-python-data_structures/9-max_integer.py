#!/usr/bin/python3
def max_integer(my_list=[]):
    max = None
    for item in my_list:
        if not max or item > max:
            max = item
    return max
