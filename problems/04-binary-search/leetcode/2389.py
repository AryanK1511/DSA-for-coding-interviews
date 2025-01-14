from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        def binary_search(target: int) -> int:
            left, right = 0, len(prefix_sum) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if prefix_sum[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right + 1

        result = []
        for query in queries:
            result.append(binary_search(query))

        return result


sol = Solution()
nums = [4, 5, 2, 1]
queries = [3, 10, 21]
print(sol.answerQueries(nums, queries))
