# You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?


def func(s: list) -> int:
    left, maxLen, zeroes = 0, 0, 0

    for right in range(len(s)):
        if s[right] == "0":
            zeroes += 1

        while zeroes > 1:
            if s[left] == "0":
                zeroes -= 1
            left += 1

        maxLen = max(maxLen, right - left + 1)

    return maxLen


s = "1101100111"
print(func(s))
