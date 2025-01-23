from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        d = deque()
        d.append(root)
        ans = []

        while d:
            temp = [0 for _ in range(len(d))]
            for i in range(len(d)):
                elem_popped = d.popleft()
                temp[i] = elem_popped.val

                if elem_popped.left:
                    d.append(elem_popped.left)

                if elem_popped.right:
                    d.append(elem_popped.right)
            ans.append(temp)
            temp = []

        return ans
