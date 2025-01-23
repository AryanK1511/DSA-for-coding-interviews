from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxValueForV = 0

        def dfs(curr, currMax, currMin):
            nonlocal maxValueForV
            if not curr:
                return

            maxValueForV = max(
                maxValueForV, abs(currMax - curr.val), abs(currMin - curr.val)
            )
            currMax, currMin = max(currMax, curr.val), min(currMin, curr.val)
            dfs(curr.left, currMax, currMin)
            dfs(curr.right, currMax, currMin)

        dfs(root, root.val, root.val)
        return maxValueForV
