from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            middle_row = top + ((bottom - top) // 2)
            if matrix[middle_row][0] > target:
                bottom = middle_row - 1
            elif matrix[middle_row][-1] < target:
                top = middle_row + 1
            else:
                left, right = 0, len(matrix[middle_row])

                while left <= right:
                    mid = left + ((right - left) // 2)

                    if matrix[middle_row][mid] > target:
                        right = mid - 1
                    elif matrix[middle_row][mid] < target:
                        left = mid + 1
                    else:
                        return True

                return False

        return False


sol = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(sol.searchMatrix(matrix, target))
