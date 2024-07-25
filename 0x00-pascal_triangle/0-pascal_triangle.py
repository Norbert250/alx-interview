#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """ Define a function `pascal_triangle(n)` that produces a list of lists, 
    where each sublist contains integers that form Pascal's triangle up to `n` rows.
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            row = []
            Column = 1
            for j in range(1, i + 1):
                row.append(Column)
                Column = Column * (i - j) // j
            triangle.append(row)
    return triangle
