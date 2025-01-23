class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0

            is_good = root.val >= maxVal
            maxVal = max(maxVal, root.val)

            left_count = dfs(root.left, maxVal)
            right_count = dfs(root.right, maxVal)

            return left_count + right_count + (1 if is_good else 0)

        return dfs(root, root.val)
