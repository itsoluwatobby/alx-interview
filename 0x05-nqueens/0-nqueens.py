#!/usr/bin/python3
"""module n-queeen"""
import sys


def valid_move(q, x, array):
    """checks if its a valid move"""
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def place_position(queen, column, prev_solution):
    """Place the queen in the respective position"""
    safePosition = []
    for i in prev_solution:
        for x in range(column):
            if valid_move(queen, x, i):
                safePosition.append(i + [x])
    return safePosition


def get_results(row, column):
    """"Gets the final result"""
    res = [[]]
    for queen in range(row):
        res = place_position(queen, column, res)
    return res


def initialize_app():
    """Project initailizer"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def main():
    """Main function to start the program"""
    n = initialize_app()
    solutions = get_results(n, n)
    for i in solutions:
        res = []
        for q, x in enumerate(i):
            res.append([q, x])
        print(res)


if __name__ == '__main__':
    main()
