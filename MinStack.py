"""Description 155. Min Stack
Medium

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods `pop`, `top`, and `getMin` will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to `push`, `pop`, `top`, and `getMin`.
"""

from typing import List

class MinStack:
    def __init__(self):
        self.stack: List[int] = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_vals or val <= self.min_vals[-1]:
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
    