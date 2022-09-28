#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for data in sorted(my_dict.keys()):
        print("{:s}: {}".format(data, my_dict[data]))
