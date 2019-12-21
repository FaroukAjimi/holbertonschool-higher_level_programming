#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    b = list(map(lambda x: list(map(lambda y: y * y, x)), matrix))
    return (b)
