from typing import List


class MinStack:
    def __init__(self):
        self.stack: List[int] = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_vals:
            self.min_vals.append(val)
        elif val <= self.min_vals[-1]:
            self.min_vals.append(val)

    def pop(self) -> None:
        item = self.stack.pop()
        if item == self.min_vals[-1]:
            self.min_vals.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1] if self.min_vals else None



if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(100)
    minStack.push(2000)
    minStack.push(4000)
    minStack.push(8000)
    minStack.push(10)
    minStack.push(80000)
    print(minStack.getMin())
    print(minStack.top())
    minStack.pop()
    print(minStack.getMin())
    print(minStack.top())
    