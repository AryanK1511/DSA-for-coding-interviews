from typing import List


class Solution:
    def trap_two_pointers(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]

        return res

    def trap_arrays(self, height: List[int]) -> int:
        if not height:
            return 0

        left_max_arr, right_max_arr, min_leftright_arr = [], [], []
        maxLeft = height[0]
        maxRight = height[len(height) - 1]
        res = 0

        for i in range(len(height)):
            if height[i] > maxLeft:
                maxLeft = height[i]
            if height[len(height) - i - 1] > maxRight:
                maxRight = height[len(height) - i - 1]
            left_max_arr.append(maxLeft)
            right_max_arr.insert(0, maxRight)

        for i in range(len(height)):
            if left_max_arr[i] > right_max_arr[i]:
                min_leftright_arr.append(right_max_arr[i])
            else:
                min_leftright_arr.append(left_max_arr[i])

        for index, h in enumerate(min_leftright_arr):
            res += h - height[index]

        return res

    def trap_self_test(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        res = 0

        while left < right:
            if max_left < max_right:
                left += 1

                if max_left - height[left] > 0:
                    res += max_left - height[left]

                max_left = max(max_left, height[left])
            else:
                right -= 1

                if max_right - height[right] > 0:
                    res += max_right - height[right]

                max_right = max(max_right, height[right])
        return res


sol = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(sol.trap_self_test(height))

"""
# Notes

### Approach 1: Two-Pointer Solution (Efficient)

Time Complexity: O(n)
Space Complexity: O(1)

Steps:

1. Initialize two pointers (`left` and `right`) at the beginning and end of the array, respectively.
2. Maintain two variables (`leftMax` and `rightMax`) to track the maximum height seen so far from both directions.
3. Compare the values of `leftMax` and `rightMax`:
   - If `leftMax` is smaller, move the `left` pointer to the right, update `leftMax` if necessary, and calculate the trapped water at the `left` position.
   - If `rightMax` is smaller or equal, move the `right` pointer to the left, update `rightMax` if necessary, and calculate the trapped water at the `right` position.
4. Continue the process until the two pointers meet.
5. Return the total trapped water.

Why this is efficient:

- This approach only requires a single pass through the array, thus the time complexity is O(n).
- It uses constant space, O(1), because only a few extra variables are needed for tracking the left and right max heights, making it very space-efficient.

### Approach 2: Array-based Solution (Inefficient)

Time Complexity: O(n)
Space Complexity: O(n)

Steps:

1. Create three arrays (`left_max_arr`, `right_max_arr`, and `min_leftright_arr`):
   - `left_max_arr[i]` stores the maximum height encountered from the left up to index `i`.
   - `right_max_arr[i]` stores the maximum height encountered from the right up to index `i`.
   - `min_leftright_arr[i]` stores the minimum value between `left_max_arr[i]` and `right_max_arr[i]`.
2. Iterate through the input array:
   - Update the `left_max_arr` and `right_max_arr` by comparing and storing the maximum values as you traverse the array from left to right and right to left, respectively.
3. Calculate the trapped water at each position using the formula: `min_leftright_arr[i] - height[i]` for each index.
4. Return the total trapped water.

Why this is inefficient:
- This approach involves multiple iterations over the array to compute the maximum heights from both directions, making it O(n) in time complexity.
- It requires O(n) space for the arrays (`left_max_arr`, `right_max_arr`, and `min_leftright_arr`), which is less space-efficient than the two-pointer approach.

### Comparison:

1. **Time Complexity**:
   - Both solutions have the same time complexity, O(n), as they both iterate through the input array.
   
2. **Space Complexity**:
   - The two-pointer solution uses O(1) space, as it only requires a few extra variables.
   - The array-based solution uses O(n) space because it requires additional arrays to store maximum heights and intermediate values.

3. **Efficiency**:
   - The two-pointer approach is more efficient in terms of space usage (O(1) space), making it a better choice for large inputs or memory-constrained environments.

"""
