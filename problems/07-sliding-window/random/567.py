class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1hmp, s2hmp = {}, {}
        left = 0

        for char in s1:
            s1hmp[char] = s1hmp.get(char, 0) + 1

        n = len(s1)
        for right in range(len(s2)):
            s2hmp[s2[right]] = s2hmp.get(s2[right], 0) + 1

            while (right - left + 1) > n:
                s2hmp[s2[left]] = s2hmp.get(s2[left], 0) - 1
                if s2hmp[s2[left]] == 0:
                    del s2hmp[s2[left]]
                left += 1

            if s2hmp == s1hmp:
                return True

        return False


sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(sol.checkInclusion(s1, s2))
