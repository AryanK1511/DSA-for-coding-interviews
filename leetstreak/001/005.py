from typing import List

# 14 January 2024
# 2657. Find the Prefix Common Array of Two Arrays
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/?envType=daily-question&envId=2025-01-14


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common_array = [0 for _ in range(n)]
        frequency = [0 for _ in range(n)]
        common_count = 0

        for index in range(n):
            frequency[A[index] - 1] += 1

            if frequency[A[index] - 1] == 2:
                common_count += 1

            frequency[B[index] - 1] += 1

            if frequency[B[index] - 1] == 2:
                common_count += 1

            prefix_common_array[index] = common_count

        return prefix_common_array


sol = Solution()
A = [1, 3, 2, 4]
B = [3, 1, 2, 4]
print(sol.findThePrefixCommonArray(A, B))
