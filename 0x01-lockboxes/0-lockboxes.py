#!/usr/bin/python3

def canUnlockAll(boxes):

    keys = set([0])
    visited = [0]

    while visited:
        current = visited.pop(0)

        for key in boxes[current]:
            if key < len(boxes) and key not in keys:
                keys.add(key)
                visited.append(key)

    return len(keys) == len(boxes)
