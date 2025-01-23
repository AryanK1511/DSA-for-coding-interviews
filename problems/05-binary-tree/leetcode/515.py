from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        d = deque()
        d.append(root)
        ans = []

        while len(d) > 0:
            maxVal = float("-inf")
            for index, elem in enumerate(d):
                if elem.val > maxVal:
                    maxVal = elem.val
            ans.append(maxVal)

            for _ in range(len(d)):
                popped_item = d.popleft()

                if popped_item.left:
                    d.append(popped_item.left)
                if popped_item.right:
                    d.append(popped_item.right)

        return ans
