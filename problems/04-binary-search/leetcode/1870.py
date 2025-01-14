from math import ceil
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1

        left, right, minSpeed = 1, 10**7, -1

        def calcHours(speed: int) -> float:
            hours = 0
            for index, d in enumerate(dist):
                if index == len(dist) - 1:
                    hours += d / speed
                else:
                    hours += ceil(d / speed)
            return hours

        while left <= right:
            mid = left + (right - left) // 2
            if calcHours(mid) > hour:
                left = mid + 1
            else:
                minSpeed = mid
                right = mid - 1

        return minSpeed


sol = Solution()
# dist = [1, 3, 2]
# hour = 1.9

dist = [1, 1, 100000]
hour = 2.01
print(sol.minSpeedOnTime(dist, hour))
