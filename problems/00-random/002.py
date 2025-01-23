from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rt, rb = 0, len(matrix) - 1
        colsize = len(matrix[0])
        n = len(matrix)
        ans = []

        def loopAndAppend(x, colsize, rev, switcher):
            if rev:
                for i in range(switcher, colsize - switcher):
                    ans.append(matrix[x][i])
                for i in range(switcher + 1, n - switcher):
                    ans.append(matrix[i][colsize - 1 - switcher])

            else:
                for i in range(colsize - switcher - 2, switcher - 1, -1):
                    ans.append(matrix[x][i])
                for i in range(n - switcher - 2, switcher, -1):
                    ans.append(matrix[i][switcher])

        switcher = 0
        ts = 0
        bs = 0
        while rt <= rb and len(ans) < n * colsize:
            if switcher % 2 == 0:
                loopAndAppend(rt, colsize, True, ts)
                ts += 1
                rt += 1
            else:
                loopAndAppend(rb, colsize, False, bs)
                bs += 1
                rb -= 1
            switcher += 1

        return ans[: n * colsize]


sol = Solution()
matrix = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
]
print(sol.spiralOrder(matrix))
