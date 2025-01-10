from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, 0, targetSum)

    def helper(self, root: Optional[TreeNode], sum: int, targetSum: int) -> bool:
        if not root:
            return sum
        self.helper(root.left, sum + root.val)
        self.helper(
            root.right,
        )
