from math import ceil
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start, end = 1, max(nums)

        def getSum(mid):
            return sum(ceil(num / mid) for num in nums)

        while start <= end:
            mid = start + ((end - start) // 2)

            if getSum(mid) > threshold:
                start = mid + 1
            else:
                end = mid - 1

        return start


sol = Solution()
nums = [1, 2, 5, 9]
threshold = 6
print(sol.smallestDivisor(nums, threshold))
