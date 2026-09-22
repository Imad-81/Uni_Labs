# Experiment 8: Dynamic Programming (DP)
# 8(a) - Matrix Chain Multiplication (MCM)
# 8(b) - Longest Common Subsequence (LCS)


# ==========================================================
# 8(a) - Matrix Chain Multiplication
# ==========================================================
def matrix_chain_multiplication(p):
    if len(p) < 2:
        return 0, []

    # Number of matrices
    n = len(p) - 1

    # Create a DP table and initialize all values to 0
    dp = [[0 for j in range(n)] for i in range(n)]

    # length represents the number of matrices being multiplied
    for length in range(2, n + 1):

        # Select the starting matrix
        for i in range(n - length + 1):

            # Calculate the ending matrix
            j = i + length - 1

            # Set the initial cost to infinity
            dp[i][j] = float('inf')

            # Try every possible position to split the matrices
            for k in range(i, j):

                # Calculate the multiplication cost
                cost = (dp[i][k] +
                        dp[k + 1][j] +
                        p[i] * p[k + 1] * p[j + 1])

                # If the new cost is smaller, update the table
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1], dp


def run_matrix_chain_multiplication():
    while True:
        try:
            n_str = input("Enter number of matrices: ").strip()
            if not n_str:
                continue
            n = int(n_str)
            if n < 1:
                print("Number of matrices must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    print(f"Enter {n + 1} dimensions (space or comma-separated):")
    p = []
    while len(p) < n + 1:
        line = input().strip()
        if not line:
            continue
        try:
            parts = line.replace(",", " ").split()
            p.extend([int(x) for x in parts])
        except ValueError:
            print("Invalid dimension! Please enter integers only.")

    p = p[:n + 1]
    min_cost, _ = matrix_chain_multiplication(p)

    # Display the minimum multiplication cost
    print("Minimum number of multiplications =", min_cost)


# ==========================================================
# 8(b) - Longest Common Subsequence (LCS)
# ==========================================================
def longest_common_subsequence(str1, str2):
    # Find the lengths of both strings
    m = len(str1)
    n = len(str2)

    # Create a DP table with 0 values
    # Rows represent characters of first string
    # Columns represent characters of second string
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    # Compare each character of the first string
    for i in range(1, m + 1):

        # Compare each character of the second string
        for j in range(1, n + 1):

            # If the characters are the same
            if str1[i - 1] == str2[j - 1]:

                # Add 1 to the previous diagonal value
                dp[i][j] = dp[i - 1][j - 1] + 1

            # If the characters are different
            else:

                # Take the maximum value from top or left
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The last cell contains the length of the LCS
    length = dp[m][n]

    # Start from the last characters to find the actual LCS
    i = m
    j = n

    # Create an empty string to store the LCS
    lcs = ""

    # Continue until we reach the beginning
    while i > 0 and j > 0:

        # If the characters are the same
        if str1[i - 1] == str2[j - 1]:

            # Add the character to the LCS
            lcs += str1[i - 1]

            # Move diagonally
            i -= 1
            j -= 1

        # If characters are different
        elif dp[i - 1][j] > dp[i][j - 1]:

            # Move up
            i -= 1

        else:

            # Move left
            j -= 1

    # Reverse the LCS because it was created backwards
    lcs = lcs[::-1]

    return lcs, length


def run_longest_common_subsequence():
    # Ask the user to enter the first string
    str1 = input("Enter first string: ").strip()

    # Ask the user to enter the second string
    str2 = input("Enter second string: ").strip()

    lcs, length = longest_common_subsequence(str1, str2)

    # Display the LCS
    print("Longest Common Subsequence =", lcs if lcs else "(none)")

    # Display the length of the LCS
    print("Length of LCS =", length)


# ==========================================================
# Built-in Demos
# ==========================================================
def demo_matrix_chain_multiplication():
    print("Demo Matrix Chain Multiplication:")
    p = [10, 20, 30, 40]
    n = len(p) - 1
    print(f"Number of matrices: {n}")
    print(f"Matrix dimensions: {p} (representing {n} matrices)")
    min_cost, _ = matrix_chain_multiplication(p)
    print("Minimum number of multiplications =", min_cost)


def demo_longest_common_subsequence():
    print("Demo Longest Common Subsequence:")
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    print(f"First string:  '{str1}'")
    print(f"Second string: '{str2}'")
    lcs, length = longest_common_subsequence(str1, str2)
    print("Longest Common Subsequence =", lcs)
    print("Length of LCS =", length)


# ==========================================================
# Main Interactive Runner
# ==========================================================
def main():
    print("==========================================================")
    print("  EXPERIMENT 8: DAA LAB - DYNAMIC PROGRAMMING (DP)")
    print("==========================================================")
    print("1. 8(a) - Matrix Chain Multiplication (MCM)")
    print("2. 8(b) - Longest Common Subsequence (LCS)")
    print("3. Run Both Experiments (Interactive)")
    print("4. Run Example / Demo Data")
    print("==========================================================")

    try:
        choice = input("Enter choice (1-4) [default: 3]: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
        return

    if not choice:
        choice = "3"

    if choice == "1":
        print("\n--- 8(a) Matrix Chain Multiplication ---")
        run_matrix_chain_multiplication()
    elif choice == "2":
        print("\n--- 8(b) Longest Common Subsequence ---")
        run_longest_common_subsequence()
    elif choice == "3":
        print("\n--- 8(a) Matrix Chain Multiplication ---")
        run_matrix_chain_multiplication()
        print("\n--- 8(b) Longest Common Subsequence ---")
        run_longest_common_subsequence()
    elif choice == "4":
        print("\n--- 8(a) Matrix Chain Multiplication (Demo) ---")
        demo_matrix_chain_multiplication()
        print("\n--- 8(b) Longest Common Subsequence (Demo) ---")
        demo_longest_common_subsequence()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
