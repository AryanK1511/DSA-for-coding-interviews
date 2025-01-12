# Leetcode Solution Notes

This is a one-stop shop for all the notes for the problems that I have solved and found to be tricky.

## 2116. Check if a Parentheses String Can Be Valid `Medium`

<https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/>

```python
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open_count = 0
        flexible_count = 0

        for i in range(len(s)):
            if locked[i] == "0":
                flexible_count += 1
            elif s[i] == "(":
                open_count += 1
            else:  # s[i] == ")"
                if open_count > 0:
                    open_count -= 1
                elif flexible_count > 0:
                    flexible_count -= 1
                else:
                    return False

        close_count = 0
        flexible_count = 0

        for i in range(len(s) - 1, -1, -1):
            if locked[i] == "0":
                flexible_count += 1
            elif s[i] == ")":
                close_count += 1
            else:  # s[i] == "("
                if close_count > 0:
                    close_count -= 1
                elif flexible_count > 0:
                    flexible_count -= 1
                else:
                    return False

        return True

```

You are given:

1. A string `s` consisting of parentheses (`(` and `)`).
2. A string `locked` of the same length as `s`, where:
   - `locked[i] == "1"` means the character `s[i]` is fixed and cannot change.
   - `locked[i] == "0"` means the character `s[i]` is flexible and can act as either `(` or `)`.

We need to determine if the string `s` can be rearranged (using the flexibility provided by `locked`) to form a valid parentheses string.

1. Every `(` must have a corresponding `)`.
2. Every `)` must have a corresponding `(`.
3. Parentheses must be balanced at every point in the string.
4. **Length Check**:

   - If the length of `s` is odd, it's impossible to balance the parentheses. Therefore, we can immediately return `False` if `len(s) % 2 != 0`.

5. **Flexibility**:

   - Flexible characters (`locked[i] == "0"`) act as "wildcards" that can be converted to either `(` or `)` as needed.

6. **Order Matters**:

   - A valid parentheses string must balance not only globally but also locally at every point in the string. For example:
     - `"(()))"` is invalid because the closing parentheses `)` at index 4 creates an imbalance before the string ends.

7. **Two Passes Are Needed**:
   - **Left-to-Right Pass**:
     - Ensures that `)` are balanced by preceding `(` or flexible characters.
   - **Right-to-Left Pass**:
     - Ensures that `(` are balanced by following `)` or flexible characters.

### Step 1: Length Check

- If `len(s) % 2 != 0`, return `False` immediately, because odd-length strings cannot form valid parentheses.

### Step 2: Left-to-Right Pass

This pass ensures that:

- Every `)` has a preceding `(` or a flexible character to balance it.

#### Variables

- `open_count`: Tracks the number of unmatched `(`.
- `flexible_count`: Tracks the number of flexible characters (`locked[i] == "0"`).

#### Logic

1. For each character in `s`:
   - If the character is flexible (`locked[i] == "0"`), increment `flexible_count`.
   - If the character is `(` (and locked), increment `open_count`.
   - If the character is `)`:
     - If `open_count > 0`, decrement `open_count` (use a preceding `(` to balance).
     - Else if `flexible_count > 0`, decrement `flexible_count` (use a flexible character to act as `(`).
     - Otherwise, return `False` (too many `)` to balance).

#### Key Point

- After this pass, the string must still be locally balanced with respect to `)`.

### Step 3: Right-to-Left Pass

This pass ensures that:

- Every `(` has a following `)` or a flexible character to balance it.

#### Variables

- `close_count`: Tracks the number of unmatched `)`.
- `flexible_count`: Tracks the number of flexible characters (`locked[i] == "0"`).

#### Logic

1. For each character in `s` (traversing from right to left):
   - If the character is flexible (`locked[i] == "0"`), increment `flexible_count`.
   - If the character is `)` (and locked), increment `close_count`.
   - If the character is `(`:
     - If `close_count > 0`, decrement `close_count` (use a following `)` to balance).
     - Else if `flexible_count > 0`, decrement `flexible_count` (use a flexible character to act as `)`).
     - Otherwise, return `False` (too many `(` to balance).

#### Key Point

- After this pass, the string must still be locally balanced with respect to `(`.

### Step 4: Final Result

If both passes complete without returning `False`, return `True`, as the string is valid.

## 20. Valid Parenthesis `Easy`

<https://leetcode.com/problems/valid-parentheses/description/>

```python
class Solution:
    def isValid(self, s: str) -> bool:
        hm = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char not in hm:
                stack.append(char)
            else:
                if stack and stack[-1] == hm[char]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
```

- The first thing to keep in mind is that this question uses a stack
- Create a mapping
- Another important thing to remember for this is that in stack questions always add a check to see if the stack is not empty

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
