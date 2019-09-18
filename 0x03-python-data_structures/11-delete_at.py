#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if index < 0 or index >= len(my_list):
        return my_list
    return my_list[:idx] + my_list[idx + 1:]
