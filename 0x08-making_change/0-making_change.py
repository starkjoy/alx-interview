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

    smallest_amounts = {coin: float('inf') for coin in coins}
    for coin in coins:
        smallest_amounts[coin] = coin

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        if amount in smallest_amounts:
            dp[amount] = 1
        else:
            for coin in coins:
                if amount >= coin:
                    dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

