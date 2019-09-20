#!/usr/bin/python3
def roman_to_int(roman):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if type(roman) != str:
        return 0
    sum = 0
    for i in range(len(roman)):
        v = values[roman[i]]
        # if letter is followed by
        if i + 1 < len(roman):
            # a letter with a greater value
            if values[roman[i + 1]] > v:
                # it is subtracted instead of added
                v = -v
        sum += v
    return sum
