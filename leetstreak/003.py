# 12 January 2024
# 2116. Check if a Parentheses String Can Be Valid
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False


sol = Solution()
# s = "(()())"
# locked = "111111"
s = "))()))"
locked = "010100"
# s = ")("
# locked = "00"
print(sol.canBeValid(s, locked))
