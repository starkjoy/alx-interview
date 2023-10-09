#!/usr/bin/python3
"""This function calculates the fewest number of operations"""


def minOperations(n):
    """
    Actual implementation

    Arguements
    n (Number): Accepts a number
    Return: Returns the number of operations as a number

    """
    if n == 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n = n // divisor
            operations = operations + divisor
        divisor = divisor + 1

    return operations
