from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height))

"""
Notes

1. Initialize two pointers, `left` at the start of the array and `right` at the end.
2. Keep track of the maximum area encountered, starting with `max_area = 0`.
3. While the left pointer is less than the right pointer:
   - Calculate the area formed by the lines at the `left` and `right` pointers: 
     `area = min(height[left], height[right]) * (right - left)`.
     - The width of the container is `right - left`, not `right - left + 1`, because the index difference already gives the correct width.
     - The height of the container is determined by the shorter of the two lines at the pointers (`min(height[left], height[right])`).
   - Update `max_area` with the larger of the current `max_area` and the calculated `area`.
4. Move the pointer that points to the shorter line inward (either `left += 1` or `right -= 1`) because moving the shorter line may help find a larger area. If the shorter line is on the left, increase `left`; otherwise, decrease `right`.
5. Repeat the process until the pointers converge.
6. Return the maximum area found.

Why use `right - left` instead of `right - left + 1`:
- The expression `right - left` gives the number of positions between the two pointers, which directly represents the width of the container.
- Adding 1 (i.e., using `right - left + 1`) would incorrectly increase the width, as the array indices are zero-based, and the width between two indices is simply the difference between them.

Time Complexity:
- The algorithm only requires one pass through the array with two pointers, making the time complexity O(n), where n is the length of the `height` array.

Space Complexity:
- The algorithm uses only a constant amount of extra space (for `left`, `right`, and `max_area`), so the space complexity is O(1).
"""
