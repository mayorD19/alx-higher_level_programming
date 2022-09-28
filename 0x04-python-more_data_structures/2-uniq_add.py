#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_nos  = 0
    unique_numbers = set(my_list)
    for x in unique_numbers:
        new_nos += x
    return new_nos
