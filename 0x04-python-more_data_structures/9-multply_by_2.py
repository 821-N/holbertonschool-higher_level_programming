#!/usr/bin/python3
def multiply_by_2(dic):
    newdic = {}
    for key in dic:
        newdic[key] = dic[key] * 2
    return newdic
