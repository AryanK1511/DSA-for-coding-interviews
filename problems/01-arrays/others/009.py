from typing import List

# https://leetcode.com/problems/number-of-ways-to-split-array/description/


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        validSplits = 0
        prefix_sum = [nums[0]]

        # We dont have to initialize an array since we can just use normal variables
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])

        for index in range(len(nums) - 1):
            left_sum = prefix_sum[index]
            right_sum = prefix_sum[-1] - prefix_sum[index]

            if left_sum >= right_sum:
                validSplits += 1

        return validSplits


sol = Solution()
nums = [10, 4, -8, 7]
print(sol.waysToSplitArray(nums))
