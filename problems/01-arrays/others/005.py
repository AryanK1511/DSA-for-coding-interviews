from typing import List

# https://leetcode.com/problems/reverse-string/


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


sol = Solution()
s = ["h", "e", "l", "l", "o"]
print(sol.reverseString(s))
print(s)
