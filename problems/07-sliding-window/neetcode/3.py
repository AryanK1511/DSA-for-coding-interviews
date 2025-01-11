class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        maxLen, left = 0, 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen


sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))
