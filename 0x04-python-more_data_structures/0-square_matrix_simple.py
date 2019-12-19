#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for a in range(len(matrix)):
        new_row = []
        for b in range(len(matrix[a])):
            new_row.append((matrix[a][b])**2)
        new_matrix.append(new_row)
    return new_matrix
