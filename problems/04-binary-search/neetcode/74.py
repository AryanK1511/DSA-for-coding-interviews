from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if target < matrix[mid][0]:
                # This means that the target is in an upper row
                high = mid - 1
            elif target > matrix[mid][len(matrix[mid]) - 1]:
                # This means that the target is in a lower row
                low = mid + 1
            else:
                # This is means that the target is either in the current row or it doesn't exist
                # Use binary search again to find the element

                inner_low, inner_high = 0, len(matrix[mid]) - 1

                while inner_low <= inner_high:
                    inner_mid = inner_low + (inner_high - inner_low) // 2

                    if matrix[mid][inner_mid] < target:
                        # This means that target is towards the right
                        inner_low = inner_mid + 1
                    elif matrix[mid][inner_mid] > target:
                        # This means that the target is towards the left
                        inner_high = inner_mid - 1
                    else:
                        return True

                return False
        return False


sol = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(sol.searchMatrix(matrix, target))
