# Leetcode Solution Notes

This is a one-stop shop for all the notes for the problems that I have solved and found to be tricky.

## 543. Diameter of a tree `Easy`

<https://leetcode.com/problems/diameter-of-binary-tree/description/>

## 112. Path Sum `Easy`

<https://leetcode.com/problems/path-sum/description/>

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], current_sum: int) -> bool:
            if not node:
                return False

            current_sum += node.value

            if not node.left and not node.right:
                return current_sum == targetSum

            left_result = dfs(node.left, current_sum)
            right_result = dfs(node.right, current_sum)

            return left_result or right_result

        return dfs(root, 0)
```

Okay so the first thing that we need to think about here, is our base case. There are two base cases here:

1. The current node is the leaf node in which case we check by knowing if node.left and nide.right are null, if they are null, then we calculate the sum at that point and return whether it is equal or not.
2. The second case is when there is no root in which case we obv return false.

Once these two cases are established we are left to figure out what to do with the cases where none of these base cases and met and that is when we do a simple dfs on the left and right subtree.

## 1448. Count Good Nodes in Binary Tree `Medium`

```python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
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
```

This one has a lot of edge cases so I will try to explain this in as much detail as possible. So the first step you have to do is think about the recursion base case:

- If there is not root then we return `0`. It makes sense because if there is no root, it means that there cannot be any good nodes as there are no nodes.

Another thing that we have to keep in mind in this question is that for each stage the logic goes something like this:

- Is it a root node?
  - Yes: Return 0
  - No:
    - Is the max value up until that point <= the current value
      - Yes: Great, we init a local counter and set it to one, we also update the max num before node to the current value and then pass it further down
      - No: We init a local counter and set it to 0
    - Call DFS on the left and right subtree and pass it the max value. You will get counts for left and right and you will add them to your local variable and then return the total count for each node
