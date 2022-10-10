#!/usr/bin/python3
"""Making a function that prints the number of items in a/
list and raising or making an exception to it.
"""
def safe_print_list(my_list=[], x=0):
    d = 0
    try:
        for i in range(x):
            print(my_list[i], end ='')
            d += 1
    except IndexError:
        None
    print()
    return d

