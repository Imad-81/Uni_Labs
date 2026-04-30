# Experiment 10: Sudoku Solver using Backtracking

"""
Aim:
To design a Python program to solve a Sudoku puzzle using backtracking and recursion, 
ensuring all constraints of rows, columns, and subgrids are satisfied.

Algorithm:
1. Start
2. Represent Sudoku as a 9x9 grid.
3. Find an empty cell.
4. Try numbers 1 to 9:
   - Check if number is valid (row, column, 3x3 box).
5. If valid -> place number.
6. Recursively solve remaining grid.
7. If conflict occurs -> backtrack (remove number).
8. Repeat until solution is found.
9. Display solved Sudoku.
10. Stop
"""

def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row, column, and the 3x3 grid
    for i in range(9):
        if (
            board[row][i] == num or
            board[i][col] == num or
            board[row - row % 3 + i // 3][col - col % 3 + i % 3] == num
        ):
            return False
    return True


def find_empty_location(board):
    # Find an empty location in the board (value 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def solve_sudoku(board):
    # Find an empty location
    empty_location = find_empty_location(board)

    # If there is no empty location, the puzzle is solved
    if not empty_location:
        return True

    row, col = empty_location

    # Try placing numbers from 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number if it's valid
            board[row][col] = num

            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # Backtrack
            board[row][col] = 0

    # If no numbers lead to a solution, backtrack
    return False


def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


if __name__ == "__main__":
    # Input a partially filled Sudoku grid (Matching the example in the lab manual)
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku Grid:")
    print_board(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Grid:")
        print_board(sudoku_grid)
    else:
        print("\nNo solution exists.")
