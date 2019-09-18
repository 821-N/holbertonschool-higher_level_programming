#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for item in my_list:
        new += [item % 2 == 0]
