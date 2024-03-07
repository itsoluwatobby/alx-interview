#!/usr/bin/python3

"""
create a function that returns a list of lists of integers representing
the Pascal's triangle of n
"""


def pascal_triangle(n):
    """Returns a list on argument n"""

    if n <= 0:
        return []

    pascalTriangle = []

    for i in range(n):
        sub_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                sub_list.append(1)
            else:
                val = pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j]
                sub_list.append(val)
        pascalTriangle.append(sub_list)

    return pascalTriangle
