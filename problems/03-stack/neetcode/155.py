class MinStack:
    def __init__(self):
        self.stack = []
        self.curr_min = float("inf")

    def push(self, val: int) -> None:
        if val < self.curr_min:
            self.curr_min = val
        self.stack.append((val, self.curr_min))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.curr_min = self.getMin()
        else:
            self.curr_min = float("inf")

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


obj = MinStack()
obj.push(5)
obj.push(2)
obj.push(8)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Notes:

The trick in this question is to push a tuple in the stack that keeps track of the min value side by side at that current point in time
"""
