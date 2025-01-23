from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        d = deque()
        d.append(root)
        level = 1

        while d:
            for _ in range(len(d)):
                popped_item = d.popleft()

                if not popped_item.left and not popped_item.right:
                    return level

                if popped_item.left:
                    d.append(popped_item.left)
                if popped_item.right:
                    d.append(popped_item.right)
            level += 1

        return level
