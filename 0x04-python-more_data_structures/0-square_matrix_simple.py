#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    d_matrix = matrix.copy()
    for row in range(len(matrix)):
        d_matrix[row] = list(map((lambda x: x**2), matrix[row]))
    return d_matrix
