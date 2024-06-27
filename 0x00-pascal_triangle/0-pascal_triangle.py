#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): Number of rows of Pascal's triangle to generate.

    Returns:
        list of lists of ints: Pascal's triangle represented as a list of lists.
                               Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

