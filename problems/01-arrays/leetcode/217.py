from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

            if hash_map[num] > 1:
                return True

        return False


s = Solution()

nums = [1, 2, 3, 1]
print(s.containsDuplicate(nums))
