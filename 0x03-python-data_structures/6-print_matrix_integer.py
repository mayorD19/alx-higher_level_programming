#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        fmt = "{} "*len(x)
        print(fmt.strip().format(*x))
