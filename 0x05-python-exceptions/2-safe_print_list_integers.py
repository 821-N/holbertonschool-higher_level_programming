#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for i in range(0, x):
            try:
                print(end="{:d}".format(my_list[i]))
                printed += 1
            except (ValueError, TypeError):
                pass
    finally:
        print()
    return printed
