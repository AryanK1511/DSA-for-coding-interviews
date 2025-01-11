from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], current_sum: int) -> bool:
            if not node:
                return False

            current_sum += node.val

            if not node.left and not node.right:
                return current_sum == targetSum

            left_result = dfs(node.left, current_sum)
            right_result = dfs(node.right, current_sum)

            return left_result or right_result

        return dfs(root, 0)
