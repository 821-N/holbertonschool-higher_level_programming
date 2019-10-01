#!/usr/bin/python3
import sys


def safe_function(fucked, *args):
    try:
        return fucked(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
