#!/usr/bin/python3
"""
0-prime_game module
"""


def is_prime(n):
    """returns true if numer is prime"""
    if (n <= 1):
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Return: name of the player that won the most rounds

    Arguments:
        x (int): rounds of games played
        nums (int[]): array of moves
    """
    winner = ''
    win = ''
    players = {'Maria': 0, 'Ben': 0}

    names = list(players.keys())
    if not len(nums):
        return None
    for num in nums:
        moves = [(i+1) for i in range(num)]
        prime_moves = []

        for move in moves:
            if is_prime(move):
                prime_moves.append(move)

        if not len(prime_moves):
            win = names[1]
        else:
            for i in range(len(prime_moves)):
                if i % 2 == 0:
                    win = names[0]
                else:
                    win = names[1]
        players[win] = players[win] + 1

    most_wins = max(players[names[0]], players[names[1]])
    winner = names[0] if players[names[0]] == most_wins else names[1]
    return winner
