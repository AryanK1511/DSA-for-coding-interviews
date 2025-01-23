from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        d = deque([root])
        ans = []
        left_to_right = True

        while d:
            level = deque()
            for _ in range(len(d)):
                node = d.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)

            ans.append(list(level))
            left_to_right = not left_to_right

        return ans
