from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        d = deque()
        d.append(root)
        ans = []

        while d:
            ans.append(d[-1].val)
            for _ in range(len(d)):
                elem = d.popleft()

                if elem.left:
                    d.append(elem.left)

                if elem.right:
                    d.append(elem.right)

        return ans
        #
