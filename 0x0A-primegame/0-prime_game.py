#!/usr/bin/python3
""" Function to determine if all boxes can be opened """


def sieve_of_eratosthenes(limit):
    """
    Generate a list of prime numbers using the Sieve of Eratosthenes algorithm.

    Parameters:
    - limit (int): The upper limit for prime numbers.

    Returns:
    - List[int]: List of prime numbers up to the given limit.
    """
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return primes


def isWinner(x, nums):
    """
    Determines the winner of a game where Maria and Ben play optimally.

    Parameters:
    - x (int): The number of rounds.
    - nums (List[int]): List of values representing 'n' for each round.

    Returns:
    - str or None: Player Name or None
    """

    def canWin(n):
        """
        Simulate the game for a given 'n' and determine if Maria can win.

        Parameters:
        - n (int): The value for the current round.

        Returns:
        - bool: True if Maria can win, False otherwise.
        """
        primes = sieve_of_eratosthenes(n)
        dp = [False] * (n + 1)
        dp[0] = dp[1] = False

        for num in range(2, n + 1):
            dp[num] = not all(dp[num - p] for p in primes if p <= num)

        return dp[n]

    # Initialize counters for Maria's and Ben's wins
    maria_wins = 0
    ben_wins = 0

    # Iterate through each round
    for n in nums:
        # Check if Maria can win for the current round
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
