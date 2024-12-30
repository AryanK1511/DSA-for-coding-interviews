from collections import defaultdict

# Anagram is a word or phrase that is formed by rearranging the letters of the original word


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        hash_map_1, hash_map_2 = defaultdict(int), defaultdict(int)

        for char in s:
            hash_map_1[char] += 1

        for char in t:
            hash_map_2[char] += 1

        return hash_map_1 == hash_map_2


"""
Time Complexity Analysis of is_anagram

1. Building hash_map_1: O(n) for iterating through string s.
2. Building hash_map_2: O(n) for iterating through string t.
3. Comparing the two hash maps: O(k), where k is the number of unique characters in s and t.

Total: O(n) + O(n) + O(k) ≈ O(n), where k ≈ n in the worst case.

Time Complexity: O(n)

Space Complexity Analysis of is_anagram:

1. Space for hash_map_1: O(k) where k is the number of unique characters in s.
2. Space for hash_map_2: O(k) where k is the number of unique characters in t.

Total: O(k) + O(k) = O(2k) ≈ O(n)

Space Complexity: O(n)
"""


sol = Solution()

s = "anagram"
t = "nagaram"
print(sol.is_anagram(s, t))
