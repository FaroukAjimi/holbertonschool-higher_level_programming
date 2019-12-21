#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = len(matrix)
    for z in range(0, a):
        if matrix and matrix[z]:
            b = [[row[i] for i in range(a)] for row in matrix]
            for i in range(a):
                for y in range(a):
                    b[i][y] = b[i][y] * b[i][y]
            return (b)
        else:
            return (0)
