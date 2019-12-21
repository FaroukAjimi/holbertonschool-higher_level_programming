#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3, 10],
    [4, 5, 6, 11],
    [7, 8, 9, 12],
    [7, 8, 9, 13]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
