#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """Create a function def generate_pascal_triangle(rows): that returns a list of lists
    of integers representing Pascal’s triangle with a given number of rows
    """
    triangle = []
    if n > 0:
        for row_num in range(1, n + 1):
            current_row = []
            value = 1
            for col_num in range(1, row_num + 1):
                current_row.append(value)
                value = value * (row_num - col_num) // col_num
            triangle.append(current_row)
    return triangle
