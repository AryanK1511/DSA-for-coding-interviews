# 15 January 2024
# 2429. Minimize XOR
# https://leetcode.com/problems/minimize-xor/description/?envType=daily-question&envId=2025-01-15


class Solution:
    def minimizeXor(num1: int, num2: int) -> int:
        set_bits_num2 = bin(num2).count("1")

        x = 0

        for i in range(31, -1, -1):
            if set_bits_num2 == 0:
                break
            if num1 & (1 << i):
                x |= 1 << i
                set_bits_num2 -= 1

        for i in range(32):
            if set_bits_num2 == 0:
                break
            if not (x & (1 << i)):
                x |= 1 << i
                set_bits_num2 -= 1

        return x


sol = Solution()
num1 = 3
num2 = 5
print(sol.minimizeXor(num1, num2))
