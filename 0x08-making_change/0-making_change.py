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

    coins.sort(reverse=True)

    i, ncoins = (0, 0)
    _total = total
    len_coins = len(coins)

    while(i < len_coins and _total > 0):
        if (_total - coins[i]) >= 0:
            _total -= coins[i]
            ncoins += 1
        else:
            i += 1

    check = _total > 0 and ncoins > 0
    return -1 if check or ncoins == 0 else ncoins
