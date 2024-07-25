#!/usr/bin/python3

def pascal_triangle(n):
    """
    If n is less than or equal to 0, return an empty list.
    """
    if n <= 0:
        return []

    """
    Initialize the first row of Pascal's triangle.
    """
    triangle = [[1]]

    """
    Generate the subsequent rows.
    """
    for i in range(1, n):
        """
        Start the new row with a 1.
        """
        row = [1]
        
        """
        Compute the inner elements of the row.
        """
        for j in range(1, i):
            """
            Each element is the sum of the two elements above it.
            """
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        """
        End the row with a 1.
        """
        row.append(1)
        
        """
        Add the completed row to the triangle.
        """
        triangle.append(row)

    return triangle
