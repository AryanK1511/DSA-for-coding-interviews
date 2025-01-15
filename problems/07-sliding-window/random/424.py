class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        left, maxFreq, ans = 0, 0, 0

        for right in range(len(s)):
            hm[s[right]] = hm.get(s[right], 0) + 1
            maxFreq = max(maxFreq, hm[s[right]])

            while ((right - left + 1) - maxFreq) > k:
                hm[s[left]] = hm.get(s[left], 0) - 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


sol = Solution()
s = "AABABBA"
k = 1
print(sol.characterReplacement(s, k))
