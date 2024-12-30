from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret_arr = []
        nums.sort()

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1

            while left < right:
                sum = num + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    ret_arr.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return ret_arr


sol = Solution()
nums = [3, 3, 0, -3, 1]
print(sol.threeSum(nums))

"""
Notes:

1. Sort the array to simplify the two-pointer approach.
2. Use a loop to iterate through the array, treating each number as the first number of a triplet.
3. Skip duplicates for the first number to avoid redundant triplets.
4. Use two pointers (left and right) to find pairs that sum with the fixed number to zero.
5. Adjust pointers based on the sum:
   - If the sum is too small, move the left pointer right.
   - If the sum is too large, move the right pointer left.
   - If a valid triplet is found, save it and skip duplicates for the second and third numbers.
6. Return the list of triplets.

Time Complexity:
- Sorting the array takes O(n log n).
- The outer loop runs O(n) times.
- For each iteration of the outer loop, the two-pointer approach runs in O(n).
- Total time complexity: O(n^2).

Space Complexity:
- The `ret_arr` list stores the output triplets. In the worst case, it could store up to O(n^3) triplets if the input array size is \( n \), though typically it will be much smaller.
- Sorting is done in-place, so it doesn't require additional space.
- Total space complexity: O(k), where \( k \) is the number of triplets stored in `ret_arr`.
"""
