from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
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
        ret_arr = []

        while len(d) > 0:
            ret_arr.append(d[-1].val)

            for i in range(len(d)):
                popped_elem = d.popleft()

                if popped_elem.left:
                    d.append(popped_elem.left)
                if popped_elem.right:
                    d.append(popped_elem.right)

        return ret_arr
