import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = 0

        def ableToEat(num):
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / num)

            return totalHours <= h

        while left <= right:
            mid = left + ((right - left) // 2)
            if ableToEat(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


sol = Solution()
piles = [3, 6, 7, 11]
h = 8
print(sol.minEatingSpeed(piles, h))
