# Given a string s, return true if it is a palindrome, false otherwise.


def checkIfPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


s = "racecar"
print(checkIfPalindrome(s))
