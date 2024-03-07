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
    subList = []

    while n != 0:

        if len(subList) < 3:
            subList.append(1)
        else:
            listLength = len(subList)
            for i in range(listLength):
                # subList = [1]
                # if i == 0:
                 #   continue
                subList.append(subList[i] + subList[i + 1])
            subList.append(1)
        pascalTriangle.append(subList)
        subList = []
        n -= 1

    return pascalTriangle
