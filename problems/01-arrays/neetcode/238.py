from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [nums[0]] * len(nums), [nums[-1]] * len(nums)
        ret_arr = []

        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
            postfix[len(nums) - i - 1] = (
                nums[len(nums) - i - 1] * postfix[len(nums) - i]
            )

        # For each element we will check the left and the right
        for i in range(len(nums)):
            if i == 0:
                ret_arr.append(postfix[i + 1])
            elif i == len(nums) - 1:
                ret_arr.append(prefix[i - 1])
            else:
                ret_arr.append(prefix[i - 1] * postfix[i + 1])

        return ret_arr


sol = Solution()
nums = [1, 2, 3, 4]
# nums = [-1, 1, 0, -3, 3]
print(sol.productExceptSelf(nums))

"""
# Notes

1. Create a prefix and postfix array
2. Keep in mind that the product except itself is simply product of everything to the left and everything to the right of the number.
3. Prefix product will give you everything to the left and postfix product will give you everything to the right of the number.
"""
