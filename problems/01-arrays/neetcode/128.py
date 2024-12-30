from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            # Check if it is the start of sequence
            if n - 1 not in num_set:
                length = 0

                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest


sol = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(sol.longestConsecutive(nums))

"""
# Notes

1. Visualize this concept like a number line.
2. If there is anything on the left that means the number is a part of a sequence. If not, then it is the start
3. If it is the start then check if the consecutive ones are there or not.
"""
