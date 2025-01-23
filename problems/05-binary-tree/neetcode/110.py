from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            True

        self.ans = True

        def dfs(root):
            if not root:
                return 0

            hl = dfs(root.left)
            hr = dfs(root.right)

            if abs(hl - hr) > 1:
                self.ans = False

            return 1 + max(hl, hr)

        dfs(root)
        return self.ans
