#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for x in range(0, len(matrix)):
        calculations = [list(map(lambda c: c**2, matrix[x]))]
        new += calculations
    return new
