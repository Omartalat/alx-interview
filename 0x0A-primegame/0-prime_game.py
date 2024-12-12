#!/usr/bin/python3
""" Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """
    Determines the winner of the prime number game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing n for each round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben"),
             or None if there is no winner.
    """
    if not nums or x < 1:
        return None

    # Determine the maximum value of n needed
    max_num = max(nums)

    # Create a sieve to find all primes up to max_num
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # Precompute the number of primes up to each number
    primes_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
