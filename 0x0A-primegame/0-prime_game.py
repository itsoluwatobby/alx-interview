#!/usr/bin/python3
"""
0-prime_game module
"""


def is_prime(n: int) -> bool:
    """returns true if numer is prime"""
    if (n <= 1):
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x: int, nums: list[int]) -> str:
    """
    Return: name of the player that won the most rounds

    Arguments:
        x (int): rounds of games played
        nums (int[]): array of moves
    """
    winner = ''
    PLAYER1, PLAYER2 = 'Maria', 'Ben'

    if not len(nums):
        return None
    for num in nums:
        moves = [(i+1) for i in range(num)]
        prime_moves = []

        for move in moves:
            if is_prime(move):
                prime_moves.append(move)

        if not len(prime_moves):
            winner = PLAYER2
        else:
            for i in range(len(prime_moves)):
                if i % 2 == 0:
                    winner = PLAYER1
                else:
                    winner = PLAYER2
    return winner
