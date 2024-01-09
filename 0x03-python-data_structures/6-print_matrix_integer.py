#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for col in row:
                print("{:di}".format(col), end=" " if col != row[-1] else '')
            print("")
    return
