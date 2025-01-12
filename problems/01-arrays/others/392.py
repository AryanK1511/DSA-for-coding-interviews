# https://leetcode.com/problems/is-subsequence/


def isSubsequence(s: str, t: str) -> bool:
    s_ptr, t_ptr = 0, 0
    count = 0

    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            count += 1
            s_ptr += 1

        t_ptr += 1

    return count == len(s)


s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
