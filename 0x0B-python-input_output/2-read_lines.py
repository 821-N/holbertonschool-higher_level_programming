#!/usr/bin/python3
"""
    2. Read n lines
"""


def read_lines(filename="", nb_lines=0):
    """ Print the first `nb_lines` lines of file `filename` """
    with open(filename) as f:
        count = 0 
        for line in f:  # why can't I write f[:nb_lines] ??
            count += 1
            if count>nb_lines:
                break
            print(end=line)
