#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = len(matrix)
    b = [[row[i] for i in range(a)]  for row in matrix]
    for i in range(a):
          b[i] = list(map(lambda x: x * x, matrix[i]))
    return (b)
