class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]: 
            self.minStack.append(x)
    def pop(self) -> None:
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()