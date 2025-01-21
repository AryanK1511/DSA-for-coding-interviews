from collections import defaultdict

# 13 January 2024
# 3223. Minimum Length of String After Operations
# https://leetcode.com/problems/minimum-length-of-string-after-operations/description/


class Solution:
    def minimumLength(self, s: str) -> int:
        offset, hmp = 0, defaultdict(int)

        for char in s:
            occurCount = hmp[char]
            occurCount += 1
            if occurCount % 3 == 0:
                offset -= 2
                occurCount -= 2
            hmp[char] = occurCount

        return len(s) + offset


sol = Solution()
s = "abaacbcbb"
print(sol.minimumLength(s))
