#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.

    * Prototype: def minOperations(n)
    * Returns an integer
    * If n is impossible to achieve, return 0
"""


def minOperations(n):
    """Returns the number of steps"""
    if n <= 1:
        return n
    steps = [0] * (n + 1)
    for i in range(2, n + 1):
        steps[i] = i
        for j in range(2, i):
            if i % j == 0:
                steps[i] = min(steps[i], steps[j] + i // j)

    return steps[n]
