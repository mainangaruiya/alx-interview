#!/usr/bin/python3
"""
min op file
"""

def minOperations(n):
    """return n if impossible or 0"""
    if n <= 1:
        return 0

        dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = i
        j = 2
        while j * j <= i:
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                dp[i] = min(dp[i], dp[i // j] + j)
            j += 1
    return dp[n]

    