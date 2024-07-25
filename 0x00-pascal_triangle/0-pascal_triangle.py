#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing Pascal’s triangle of n.
    Returns an empty list if n <= 0.
    You can assume n will always be an integer.
    """
    # Initialize an empty list to hold the rows of Pascal's triangle
    triangle = []
    
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return triangle
    
    # Generate the rows of Pascal's triangle
    for row_num in range(n):
        # Initialize the current row with the first element as 1
        current_row = [1]
        
        # Compute the inner elements of the current row
        if row_num > 0:
            for col_num in range(1, row_num):
                # Each element is the sum of the two elements above it
                current_row.append(triangle[row_num - 1][col_num - 1] + triangle[row_num - 1][col_num])
            
            # End the current row with a 1
            current_row.append(1)
        
        # Append the current row to the triangle
        triangle.append(current_row)
    
    return triangle
