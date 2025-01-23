from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        d = deque()
        d.append(root)
        count = 0

        while d:
            count = 0
            for _ in range(len(d)):
                elem = d.popleft()
                count += elem.val

                if elem.left:
                    d.append(elem.left)

                if elem.right:
                    d.append(elem.right)

        return count
