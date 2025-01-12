class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        window_count = {}
        left = 0

        for right in range(len(s2)):
            char = s2[right]
            window_count[char] = window_count.get(char, 0) + 1

            if right - left + 1 > len(s1):
                left_char = s2[left]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]
                left += 1

            if window_count == s1_count:
                return True

        return False


s1 = "ab"
s2 = "eidbaooo"
sol = Solution()
print(sol.checkInclusion(s1, s2))
