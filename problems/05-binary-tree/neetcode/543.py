from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return (
            self.diameterOfBinaryTree(self.left)
            + self.diameterOfBinaryTree(self.right)
            + 1
        )
