#!/usr/bin/python3
"""
A program that solves the N queens problem.
"""


import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at a specific position on the chessboard

    Args:
        board (list): The chessboard represented as a 2D list.
        row (int): The current row for queen placement.
        col (int): The current column for queen placement.
        N (int): The size of the chessboard.

    Returns:
        bool: True if its safe to place the queen or False otherwise.
    """

    for i  in range(col):
        if board[row][i] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True


def solve_nqueens(N):
    """
    Find and print all solutions to the N-Queens problem for a given board size N.

    Args:
        N (int): The size of the chessboard and the number of queens to be placed.
    """

    def print_solution(board):
        """
        Print the current state of the chessboard as a possible solution.

        Args:
            board (list): The chessboard represented as a 2D list.
        """
        for row in board:
            print("".join("Q" if cell else "." for cell in row))
        print()

    def backtrack(board, col):
        """
        Recursively explore possible queen placements on the chessboard.

        Args:
            board (list): The chessboard represented as a 2D list.
            col (int): The current column for queen placement.
        """
        if col == N:
            # All queens have been placed, print the solution
            print_solution(board)
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(board, col + 1)
                board[row][col] = 0

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    backtrack(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
        