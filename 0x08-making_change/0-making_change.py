#!/usr/bin/python3
"""
0-making_change.py module
"""


def makeChange(coins: list[int], total: int) -> int:
    """Returns the list fewest number of cooins needed to meet the
    the given total

    Arguments:
        coins(list): first argument
        total(int): second argument
    """
    if total <= 0:
        return 0

    # store the minimum number of coins needed for each total value in a list
    minVals = [float('inf')] * (total + 1)
    minVals[0] = 0

    for coin in coins:
        # Update dp[i] for all i >= coin
        for i in range(coin, total + 1):
            minVals[i] = min(minVals[i], minVals[i - coin] + 1)

    # if minVals[total] = infinity,it means total cannot be met by any
    # number of coins
    if minVals[total] == float('inf'):
        return -1
    else:
        return minVals[total]
