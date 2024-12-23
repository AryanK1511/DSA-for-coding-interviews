from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [nums[0]]
        ret_arr = []

        for i in range(1, len(nums)):
            print(prefix_prod)
            if nums[i] == 0:
                prefix_prod.append(prefix_prod[i - 1] * 1)
            else:
                prefix_prod.append(prefix_prod[i - 1] * nums[i])

        for i in range(len(nums)):
            print(ret_arr)
            if nums[i] == 0:
                ret_arr.append(int(prefix_prod[-1] / 1))
            else:
                ret_arr.append(int(prefix_prod[-1] / nums[i]))

        return ret_arr


sol = Solution()
nums = [1, 2, 3, 4, 5]
# nums = [-1, 1, 0, -3, 3]
print(sol.productExceptSelf(nums))
