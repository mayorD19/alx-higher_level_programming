#!/usr/bin/python3
def max_integer(my_list=[]):
    High_score = 0
    for score in my_list:
        if len(my_list) == 0:
            return None
        if (score > High_score):
            High_score = score
    return High_score

