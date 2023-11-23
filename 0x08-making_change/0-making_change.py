#!/usr/bin/python3
"""
This module contains a function to determine the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.

    Parameters:
        coins (list of int): A list of integers representing the values of available coins.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If total is 0 or less, return 0.
             If total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

# Example usage:
if __name__ == "__main__":
    coins = [1, 2, 5]
    total = 11
    result = makeChange(coins, total)
    print(result)  # Output: 3 (11 = 5 + 5 + 1)
