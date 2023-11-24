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
    if total <= 0:
        return 0

    if len(coins) <= 0:
        return 0
    
    coins.sort(reverse=True)
    
    count = 0
    
    for coin in coins:
        count += total // coin
        total %= coin
        
    return count

