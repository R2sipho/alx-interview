#!/usr/bin/python3
"""Defines a function to calculate the perimeter of an island in a grid."""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    The grid represents water with 0 and land with 1.
    
    Args:
        grid (list of list of ints): A 2D grid representing the map.
    
    Returns:
        int: The perimeter of the island.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if j > 0 and grid[i][j - 1] == 1:
                    edges += 1
                if i > 0 and grid[i - 1][j] == 1:
                    edges += 1
                    
    return size * 4 - edges * 2

