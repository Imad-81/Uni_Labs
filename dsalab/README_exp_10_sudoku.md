# Experiment 10: Sudoku Solver using Backtracking

**Aim:** To design a Python program to solve a Sudoku puzzle using backtracking and recursion, ensuring all constraints of rows, columns, and subgrids are satisfied.

**Algorithm:**
1. **Start**
2. **Represent** the Sudoku puzzle as a 9x9 grid.
3. **Find** an empty cell (represented by 0).
4. **Try** numbers 1 to 9 in the empty cell:
   - Check if the number is **valid** in the current row, column, and 3x3 box.
5. If **valid**, place the number in the cell.
6. **Recursively** attempt to solve the remaining grid.
7. If a **conflict** occurs (no number fits), **backtrack** by removing the number and trying the next one.
8. **Repeat** until a solution is found or all possibilities are exhausted.
9. **Display** the solved Sudoku grid.
10. **Stop**

**Output:**
```
Original Sudoku Grid:
5 3 0 0 7 0 0 0 0 
6 0 0 1 9 5 0 0 0 
0 9 8 0 0 0 0 6 0 
8 0 0 0 6 0 0 0 3 
4 0 0 8 0 3 0 0 1 
7 0 0 0 2 0 0 0 6 
0 6 0 0 0 0 2 8 0 
0 0 0 4 1 9 0 0 5 
0 0 0 0 8 0 0 7 9 

Solved Sudoku Grid:
5 3 4 6 7 8 9 1 2 
6 7 2 1 9 5 3 4 8 
1 9 8 3 4 2 5 6 7 
8 5 9 7 6 1 4 2 3 
4 2 6 8 5 3 7 9 1 
7 1 3 9 2 4 8 5 6 
9 6 1 5 3 7 2 8 4 
2 8 7 4 1 9 6 3 5 
3 4 5 2 8 6 1 7 9 
```
