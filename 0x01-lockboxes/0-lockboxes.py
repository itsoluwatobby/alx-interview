#!/usr/bin/python3
"""
Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """A function that determines if a box is opened or closed"""
    keys = set([0])
    visited = [0]

    while visited:
        current = visited.pop(0)

        for i in boxes[current]:
            if i < len(boxes) and i not in keys:
                keys.add(i)
                visited.append(i)

    return len(keys) == len(boxes)
