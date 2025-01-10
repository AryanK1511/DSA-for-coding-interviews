# 10 January 2024
# 916. Word Subsets
# https://leetcode.com/problems/word-subsets/description/?envType=daily-question&envId=2025-01-10

from collections import defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ret_arr = []
        char_freq = defaultdict(int)

        for word in words2:
            word_freq = defaultdict(int)
            for char in word:
                word_freq[char] += 1
            for char, freq in word_freq.items():
                char_freq[char] = max(char_freq[char], freq)

        for word in words1:
            char_freq_in_word = defaultdict(int)
            for char in word:
                if char in char_freq:
                    char_freq_in_word[char] += 1

            is_universal = True
            for char in char_freq:
                if (
                    char not in char_freq_in_word
                    or char_freq_in_word[char] < char_freq[char]
                ):
                    is_universal = False
                    break

            if is_universal:
                ret_arr.append(word)

        return ret_arr


sol = Solution()
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["lo", "eo"]
print(sol.wordSubsets(words1, words2))
