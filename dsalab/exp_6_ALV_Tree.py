# Define a node of the AVL Tree
class TreeNode:
    def __init__(self, key, value):
        self.key = key              # Key used for comparison (like category name)
        self.value = value          # Actual data stored
        self.left = None            # Pointer to left child
        self.right = None           # Pointer to right child
        self.height = 1             # Height of node (important for balancing)


# Define the AVL Tree class
class AVLTree:
    def __init__(self):
        self.root = None            # Initially tree is empty

    # Function to get height of a node
    def height(self, node):
        if node is None:
            return 0               # Height of empty node is 0
        return node.height

    # Function to calculate balance factor
    # balance = height(left subtree) - height(right subtree)
    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Right rotation (used when tree becomes left heavy)
    def rotate_right(self, y):
        x = y.left                # Left child becomes new root
        T2 = x.right              # Store right subtree of x

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights after rotation
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x                  # Return new root

    # Left rotation (used when tree becomes right heavy)
    def rotate_left(self, x):
        y = x.right              # Right child becomes new root
        T2 = y.left              # Store left subtree of y

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights after rotation
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y                 # Return new root

    # Insert a new node into AVL Tree
    def insert(self, root, key, value):
        # Step 1: Perform normal BST insertion
        if root is None:
            return TreeNode(key, value)

        if key < root.key:
            root.left = self.insert(root.left, key, value)
        elif key > root.key:
            root.right = self.insert(root.right, key, value)
        else:
            return root  # Duplicate keys are not allowed

        # Step 2: Update height of current node
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # Step 3: Get balance factor to check whether node became unbalanced
        balance = self.balance(root)

        # Step 4: Perform rotations based on cases

        # Case 1: Left Left (LL) Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Case 2: Left Right (LR) Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Case 3: Right Right (RR) Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Case 4: Right Left (RL) Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root  # Return unchanged node pointer

    # Public method to insert category
    def insert_category(self, key, value):
        self.root = self.insert(self.root, key, value)

    # Recursive search function
    def search_category(self, root, key):
        if root is None or root.key == key:
            return root           # Return node if found

        if key < root.key:
            return self.search_category(root.left, key)  # Search left

        return self.search_category(root.right, key)     # Search right

    # Public search method
    def search(self, key):
        return self.search_category(self.root, key)


# -------------------------------
# Example Usage
# -------------------------------

# Create AVL Tree object
avl_tree = AVLTree()

# Insert categories into AVL Tree
avl_tree.insert_category("Electronics", "Category: Electronics")
avl_tree.insert_category("Clothing", "Category: Clothing")
avl_tree.insert_category("Books", "Category: Books")

# Search for a category
search_result = avl_tree.search("Clothing")

# Display result
if search_result:
    print(f"Category found: {search_result.value}")
else:
    print("Category not found.")