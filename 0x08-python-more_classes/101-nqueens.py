#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    # Check if it's safe to place a queen at board[row][col]
    
    # Check the left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0] * n for _ in range(n)]
    solutions = []

    def solve(board, col):
        if col >= n:
            solution = []
            for row in board:
                solution.append("".join("Q" if cell == 1 else "." for cell in row))
            solutions.append(solution)
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0  # Backtrack

    solve(board, 0)

    for solution in solutions:
        for row in solution:
            print(row)
        print()

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
