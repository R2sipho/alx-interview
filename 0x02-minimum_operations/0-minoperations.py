#!/usr/bin/python3
""" Script that computes the minimum number of operations
    needed in a Copy All - Paste task
"""

def minOperations(n):
    """
    Method to compute the minimum number of operations for the task Copy All and Paste.

    Args:
        n: The target number to reach through the operations.

    Returns:
        The minimum number of operations required.
    """
    if n < 2:
        return 0
    
    factor_list = []
    factor_sum = 0
    i = 2
    
    while n > 1:
        if n % i == 0:
            while n % i == 0:
                n //= i
                factor_list.append(i)
                factor_sum += i
        i += 1
    
    return factor_sum

