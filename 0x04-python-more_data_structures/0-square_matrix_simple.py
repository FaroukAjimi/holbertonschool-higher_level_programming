#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = len(matrix)
    b = [[row[i] for i in range(3)] for row in matrix]
    for i in range(0, a):
        for y in range(0, a):
            b[i][y] = b[i][y] * b[i][y]
    return (b)
