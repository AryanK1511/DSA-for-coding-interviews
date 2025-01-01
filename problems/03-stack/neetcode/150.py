from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid_operators = ["+", "-", "*", "/"]

        for index, value in enumerate(tokens):
            if value in valid_operators:
                # pop the last two values and apply the operator on them
                operand_two = int(stack.pop())
                operand_one = int(stack.pop())
                result = 0

                if value == "+":
                    result = operand_one + operand_two
                elif value == "-":
                    result = operand_one - operand_two
                elif value == "*":
                    result = operand_one * operand_two
                elif value == "/":
                    result = int(operand_one / operand_two)

                value = result

            stack.append(value)

        return int(stack[0])


sol = Solution()
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(sol.evalRPN(tokens))

"""
Notes:

# The trick in this question is to understand how this math works
# You store everyvalue in the stack until you see an operator and then you pop the last two elements apply the operation on them and store the result in the stack instead of the last twp elements
"""
