#!/usr/bin/python3
"""
perimeter of the island - module:
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid

    Argument:
        grid(list): list of integers(1s and 0s)
            0 - represents water
            1 - represents land
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
