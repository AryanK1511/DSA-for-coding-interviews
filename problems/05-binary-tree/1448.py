class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root: TreeNode, maxNumBeforeNode: int):
            if not root:
                return 0

            count = 0
            if maxNumBeforeNode <= root.val:
                count += 1
                maxNumBeforeNode = root.val

            count += dfs(root.left, maxNumBeforeNode, count)
            count += dfs(root.right, maxNumBeforeNode, count)

            return count

        return dfs(root, root.val)
