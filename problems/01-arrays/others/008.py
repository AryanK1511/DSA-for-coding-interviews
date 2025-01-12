from typing import List

# https://leetcode.com/problems/subarray-product-less-than-k/


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, numSubArrs, prod = 0, 0, 1

        for right in range(len(nums)):
            prod *= nums[right]
            while left <= right and prod >= k:
                prod /= nums[left]
                left += 1
            numSubArrs += right - left + 1

        return numSubArrs


sol = Solution()
nums = [1, 2, 3]
k = 0
print(sol.numSubarrayProductLessThanK(nums, k))
