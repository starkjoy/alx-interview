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
import heapq

    if total <= 0:
        return 0

    dp = []
    heapq.heapify(dp)
    heapq.heappush(dp, (0, 0))

    while dp:
        count, amount = heapq.heappop(dp)
        if amount == total:
            return count

        for coin in coins:
            if amount + coin <= total:
                heapq.heappush(dp, (count + 1, amount + coin))

    return -1


