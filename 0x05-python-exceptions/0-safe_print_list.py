#!/usr/bin/python3
"""Making a function that prints the number of items in a/
list and raising or making an exception to it.
"""
def safe_print_list(my_list=[], x=0):
    a = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            a += 1
    except IndexError:
        None
    print()
    return a
