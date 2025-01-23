from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def helper(node):
            if not node:
                return 0

            nonlocal ans
            hl = helper(node.left)
            hr = helper(node.right)
            dia = hl + hr
            ans = max(ans, dia)
            return max(hl, hr) + 1

        helper(root)
        return ans
