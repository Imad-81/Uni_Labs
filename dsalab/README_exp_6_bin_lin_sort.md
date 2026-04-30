# Experiment 6: Linear and Binary Search Comparison

**Aim:** To implement and compare the performance of Linear Search and Binary Search algorithms on a product dataset.

**Algorithm:**
1. **Linear Search**:
   - Iterate through the list element by element.
   - Compare each product's name with the target name.
   - Time Complexity: $O(n)$.
2. **Binary Search**:
   - Sort the list by product name first.
   - Repeatedly divide the search space in half.
   - Compare the middle element with the target.
   - Time Complexity: $O(\log n)$ (excluding sorting time).
3. Provide a user interface to input search queries and display results from both algorithms.

**Key Features:**
- Case-insensitive search functionality.
- Demonstrates the necessity of sorting for binary search.
- Interactive user input for real-time testing.
