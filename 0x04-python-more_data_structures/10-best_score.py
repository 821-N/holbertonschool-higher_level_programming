#!/usr/bin/python3
def best_score(dic):
    if len(dic):
        return max(dic, key=dic.get)
