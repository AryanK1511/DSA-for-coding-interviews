from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0

            hl, dl = dfs(root.left)
            hr, dr = dfs(root.right)
            return 1 + max(hl, hr), max(hl + hr, dl, dr)

        _, dia = dfs(root)
        return dia
