# 1. Define the node class that can hold left + right pointers and a value
class Node:
    def __init__(self, value=None):
        self.value, self.left, self.right = value, None, None


# 2. Define the BinaryTree class that has a root which will not point to anything initially
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        self._insert(self.root, value)

    def _insert(self, root, value):
        if not root:
            self.root = Node(value)
            return
        if root.left:
            pass
