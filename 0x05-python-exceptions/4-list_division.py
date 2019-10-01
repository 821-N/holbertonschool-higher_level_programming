#!/usr/bin/python3
def list_division(list_1, list_2, list_length):
    result = [0] * list_length
    try:
        for i in range(0, list_length):
            try:
                result[i] = list_1[i] / list_2[i]
            except ZeroDivisionError:
                print("division by 0")
            except (TypeError, ValueError):
                print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return result
