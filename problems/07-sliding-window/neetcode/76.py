class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        thmp, shmp = {}, {}

        for char in t:
            thmp[char] = thmp.get(char, 0) + 1

        thmpKeys = thmp.keys()

        left = 0
        ans = ""

        for right, elem in enumerate(s):
            if elem in thmp:
                shmp[elem] = shmp.get(elem, 0) + 1
            print("BEFORE:", shmp, thmp, left, right)

            if shmp.get(elem, 0) > thmp.get(elem, 0):
                while left <= right:
                    if s[left] in thmp:
                        if shmp.get(s[left], 0) - 1 < 1:
                            break
                        else:
                            if shmp.keys() == thmpKeys:
                                shmp[s[left]] = shmp[s[left]] - 1
                            else:
                                break
                    left += 1
            print("AFTER:", shmp, thmp, left, right)

            if shmp.keys() == thmpKeys:
                while s[left] not in shmp:
                    left += 1

                equal = True
                for elem in thmp:
                    if thmp[elem] > shmp.get(elem, 0):
                        equal = False

                if len(ans) == 0:
                    ans = s[left : right + 1] if equal else ans
                else:
                    if len(s[left : right + 1]) <= len(ans):
                        ans = s[left : right + 1] if equal else ans

        return ans


sol = Solution()
# s = "ADOBECODEBANCDE"
# t = "ABC"
# s = "a"
# t = "aa"
# s = "ab"
# t = "a"
# s = "ab"
# t = "b"
# s = "bbaa"
# t = "aba"
s = "aaabbaaba"
t = "abbb"
print(sol.minWindow(s, t))
