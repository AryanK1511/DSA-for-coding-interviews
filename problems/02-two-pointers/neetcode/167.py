from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left <= right:
            if numbers[right] + numbers[left] > target:
                right -= 1
            elif numbers[right] + numbers[left] < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return [-1, -1]


sol = Solution()
numbers = [2, 7, 11, 15]
target = 9
print(sol.twoSum(numbers, target))
