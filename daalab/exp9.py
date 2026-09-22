# Experiment 9: Backtracking
# 9(a) - N-Queens Problem
# 9(b) - Sum of Subsets Problem


# ==========================================================
# 9(a) - N-Queens Problem (Backtracking)
# ==========================================================

def is_safe(board, row, col, n):
    # Check all previously placed queens in the same column
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens(board, row, n):
    # If all queens have been placed, a solution is found
    if row == n:
        return True

    # Try placing a queen in every column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_n_queens(board, row + 1, n):
                return True
            board[row] = -1  # backtrack
    return False


def run_n_queens():
    n = int(input("Enter the number of queens: "))
    board = [-1] * n
    if solve_n_queens(board, 0, n):
        print("\nSolution:")
        for i in range(n):
            row = ["." for _ in range(n)]
            row[board[i]] = "Q"
            print(" ".join(row))
    else:
        print("No solution exists.")


# ==========================================================
# 9(b) - Sum of Subsets using Backtracking
# ==========================================================

def sum_of_subsets(numbers, target, index, current_subset, current_sum):
    # Check whether the current sum is equal to the target
    if current_sum == target:
        print(current_subset)
        return

    # Stop if all numbers have been considered
    if index == len(numbers):
        return

    # Stop if the current sum becomes greater than the target
    if current_sum > target:
        return

    # Include the current number in the subset
    current_subset.append(numbers[index])
    sum_of_subsets(numbers, target, index + 1, current_subset, current_sum + numbers[index])

    # Remove the current number to backtrack
    current_subset.pop()
    sum_of_subsets(numbers, target, index + 1, current_subset, current_sum)


def run_sum_of_subsets():
    n = int(input("Enter the number of elements: "))
    numbers = list(map(int, input("Enter the elements: ").split()))
    target = int(input("Enter the target sum: "))
    print("\nSubsets whose sum is", target, ":")
    sum_of_subsets(numbers, target, 0, [], 0)


# ==========================================================
# Main Interactive Runner
# ==========================================================
def main():
    print("==========================================================")
    print("  EXPERIMENT 9: DAA LAB - BACKTRACKING")
    print("==========================================================")
    print("1. 9(a) - N-Queens Problem")
    print("2. 9(b) - Sum of Subsets Problem")
    print("3. Run Both Experiments (Interactive)")
    print("==========================================================")

    choice = input("Enter choice (1-3) [default: 3]: ").strip()
    if not choice:
        choice = "3"

    if choice in ["1", "3"]:
        print("\n--- 9(a) N-Queens ---")
        run_n_queens()

    if choice in ["2", "3"]:
        print("\n--- 9(b) Sum of Subsets ---")
        run_sum_of_subsets()


if __name__ == "__main__":
    main()