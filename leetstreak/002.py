# 11 January 2024
# 1400. Construct K Palindrome Strings
# https://leetcode.com/problems/construct-k-palindrome-strings/description/?envType=daily-question&envId=2025-01-11


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Condition 1: Check if k is greater than the length of s
        if k > len(s):
            return False

        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        odd_count = 0
        for count in freq.values():
            if count % 2 != 0:
                odd_count += 1

        # Condition 2: The number of odd-count characters must not exceed k
        return odd_count <= k


sol = Solution()
s = "yzyzyzyzyzyzyzy"
k = 2
print(sol.canConstruct(s, k))
