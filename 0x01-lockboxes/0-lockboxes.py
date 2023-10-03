#!/usr/bin/python3
""" Function to determine if all boxes can be opened """

def canUnlockAll(boxes):
    """ 
    Actual implementation of the function

    Arguments:
        boxes: (list of lists)
    """
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited:
                stack.append(key)

    return len(visited) == n
