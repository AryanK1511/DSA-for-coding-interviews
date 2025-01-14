from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        output = [0 for _ in range(len(spells))]
        potions.sort()
        for index, spell in enumerate(spells):
            count = self.findMatchCount(potions, success, spell)
            output[index] = count

        return output

    def findMatchCount(self, potions: List[int], target: int, num: int):
        left, right = 0, len(potions) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if num * potions[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return len(potions) - left


sol = Solution()
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(sol.successfulPairs(spells, potions, success))
