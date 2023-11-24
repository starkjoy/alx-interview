#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to match an amount
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.

    Parameters:
        coins (list of int): A list of available coins.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If total is 0 or less, return 0.
             If total cannot be met by any number of coins, return -1.
    """

    if len(coins) <= 0 or total <= 0:
        return 0
    
    coins.sort()
    
    count = 0
    
    index = len(coins) - 1
    
    while total > 0 and index >= 0:
        if coins[index] <= total:
            count += total // coins[index]
            total %= coins[index]
        index -= 1
    
    return count
