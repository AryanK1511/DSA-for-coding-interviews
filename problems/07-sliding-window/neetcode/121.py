from typing import List


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
