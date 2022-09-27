#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        fmt = "{:d} "*len(x)
        print(fmt.strip().format(*x))
