class TreeNode:
    def __init__(self, key, value):
        self.key, self.value, self.left, self.right, self.height = key, value, None, None, 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _get_h(self, n): return n.height if n else 0
    def _get_b(self, n): return self._get_h(n.left) - self._get_h(n.right) if n else 0

    def _rotate(self, y, left=True):
        x = y.right if left else y.left
        T2 = x.left if left else x.right
        if left: x.left, y.right = y, T2
        else: x.right, y.left = y, T2
        y.height = 1 + max(self._get_h(y.left), self._get_h(y.right))
        x.height = 1 + max(self._get_h(x.left), self._get_h(x.right))
        return x

    def insert(self, key, value, node=None, first_call=True):
        if first_call: self.root = self.insert(key, value, self.root, False); return
        if not node: return TreeNode(key, value)
        if key < node.key: node.left = self.insert(key, value, node.left, False)
        elif key > node.key: node.right = self.insert(key, value, node.right, False)
        else: return node

        node.height = 1 + max(self._get_h(node.left), self._get_h(node.right))
        b = self._get_b(node)

        if b > 1:
            if key > node.left.key: node.left = self._rotate(node.left, True)
            return self._rotate(node, False)
        if b < -1:
            if key < node.right.key: node.right = self._rotate(node.right, False)
            return self._rotate(node, True)
        return node

    def search(self, key, node=None, first_call=True):
        curr = self.root if first_call else node
        if not curr or curr.key == key: return curr
        return self.search(key, curr.left if key < curr.key else curr.right, False)

# Example Usage
avl = AVLTree()
for k, v in [("Electronics", "Electronics"), ("Clothing", "Clothing"), ("Books", "Books")]:
    avl.insert(k, f"Category: {v}")

res = avl.search("Clothing")
print(f"Category found: {res.value}" if res else "Category not found.")