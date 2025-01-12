# https://leetcode.com/problems/valid-parentheses/description/


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


sol = Solution()
s = "({[[]})"
print(sol.isValid(s))
