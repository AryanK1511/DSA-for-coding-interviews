from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            sorted_str = "".join(sorted(word))

            if sorted_str not in hash_map:
                hash_map[sorted_str] = []

            hash_map[sorted_str].append(word)

        return list(hash_map.values())


sol = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(strs))
