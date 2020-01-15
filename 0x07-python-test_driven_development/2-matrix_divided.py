#!/usr/bin/python3
"""Module to divid a matrix by a number
A list of lists should exist
division cant be by Zero
element of the matrix should be integers
if they are float they need to be casted to int"""


def matrix_divided(matrix, div):
    """function matrix_divided
    args: matrix
    :div"""
    m = []
    l = 'matrix must be a matrix (list of lists) of integers/floats'
    z = 'Each row of the matrix must have the same size'
    a = None
    if not(isinstance(div, (float, int))):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not(isinstance(matrix, list)):
        raise TypeError(l)

    for i in range(len(matrix)):
        if not(isinstance(matrix[i], list)):
            raise TypeError(l)
        if (a is not None):
            if (a != len(matrix[i])):
                raise TypeError(z)
        a = len(matrix[i])
        for y in range(len(matrix[i])):
            if isinstance(matrix[i][y], (int, float)) is False:
                raise TypeError(l)

    for i in range(len(matrix)):
        m.append([])

    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            m[i].append(round(matrix[i][y]/div, 2))
    return(m)
