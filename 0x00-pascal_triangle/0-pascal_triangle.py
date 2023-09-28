#!/usr/bin/python3
""" This is a function that returns a pascal triangle representation """


def pascal_triangle(n):
    """ Prints integers reperesenting pascals triangle """
    if (n <= 0):
        return []
    if (n == 1):
        return [[1]]

    # Creates an array container to store values
    triangle = []
    # Creates the first row in the container
    triangle.append([1])

    # Creates the rest of the rows as needed
    for r in range(1, n):
        prev_row = triangle[r - 1]
        row = [1]
        for c in range(1, r):
            middle_value = prev_row[c - 1] + prev_row[c]
            row.append(middle_value)
        row.append(1)
        triangle.append(row)

    return triangle
