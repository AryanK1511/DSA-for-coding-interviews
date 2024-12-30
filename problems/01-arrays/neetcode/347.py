from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        # Now, I need to sort the hashmap according to the values
        sorted_hashmap = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

        ret_arr = []
        for elem in sorted_hashmap[:k]:
            ret_arr.append(elem[0])

        return ret_arr


sol = Solution()

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(sol.topKFrequent(nums, k))
