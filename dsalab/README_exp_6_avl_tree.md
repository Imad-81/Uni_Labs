# Experiment 6: AVL Tree Implementation

**Aim:** To implement a height-balanced AVL Tree to categorize and search e-commerce items efficiently.

**Algorithm:**
1. Define a `TreeNode` with `key`, `value`, `left child`, `right child`, and `height`.
2. Implement **Rotations**:
   - **Rotate Right (LL Case):** If the left subtree becomes too deep.
   - **Rotate Left (RR Case):** If the right subtree becomes too deep.
   - **Double Rotations (LR/RL Cases):** Combine rotations for complex imbalances.
3. Implement **Insertion**:
   - Perform standard BST insertion.
   - Update node height and check the balance factor ($H_{left} - H_{right}$).
   - Re-balance the tree using rotations if the factor is not $-1, 0, 1$.
4. Implement **Search**: Traverse the tree recursively based on key comparison ($O(\log n)$).

**Output:**
Category found: Category: Clothing
