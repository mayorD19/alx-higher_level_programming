#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_nos  = 0
    for x in set(my_list):
        new_nos += x
    return new_nos
