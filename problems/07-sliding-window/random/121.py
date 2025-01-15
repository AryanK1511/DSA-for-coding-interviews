from typing import List

"""
prices = [7, 1, 5, 3, 6, 4]
b = 7, s = 7 p = 0

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        bp = 0

        for sp in range(1, len(prices)):
            if prices[sp] < prices[bp]:
                bp = sp
            else:
                maxProf = max(maxProf, prices[sp] - prices[bp])

        return maxProf


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))
