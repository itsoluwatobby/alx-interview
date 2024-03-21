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
    if n < 2:
        return 0
    ops, steps = 0, 2
    while steps <= n:
        if n % steps == 0:
            ops += steps
            n = n / steps
            steps -= 1
        steps += 1

    return ops
