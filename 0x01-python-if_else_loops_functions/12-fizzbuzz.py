#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100 + 1):
        if i % 3 == 0:
            print(end="Fizz")
        if i % 5 == 0:
            print(end="Buzz")
        if i % 3 and i % 5:
            print(end="{:d}".format(i))
        print(end=" ")
