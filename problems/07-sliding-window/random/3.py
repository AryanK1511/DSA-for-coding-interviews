"""
Thought Process:

Count = Hashmap with only one count = Set
a b c a b c b b

set ()
maxSubstr = 0
right ++
while elem in set
    remove elem from set on left
    left ++
maxSubstr = max (ms, left - right + 1)
return ms
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        elemSet = set()
        maxSubstr, left = 0, 0

        for right in range(len(s)):
            while s[right] in elemSet:
                elemSet.remove(s[left])
                left += 1
            elemSet.add(s[right])

            maxSubstr = max(maxSubstr, right - left + 1)

        return maxSubstr


sol = Solution()
s = "bbbbb"
print(sol.lengthOfLongestSubstring(s))
