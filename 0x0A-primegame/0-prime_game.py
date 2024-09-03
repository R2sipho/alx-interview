#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    if x <= 0 or not nums or x != len(nums):
        return None

    ben, maria = 0, 0
    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_num + 1, i):
                is_prime[multiple] = False

    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime[i] else 0)

    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    return None

