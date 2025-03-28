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

from typing import List, Tuple

class MinStack2:
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
    
# Commands: push 11, push 11, push 2, push 11, push 2, pop, top, get_min,pop
# Stack: [11, 11, 2]
# mins: [[11, 2], [2, 1]]
# Returns: top - 11,get_min - 2
class MinStack:
    def __init__(self):
        self.values = []
        self.min_values = []
        
    
    def push(self, val: int) -> None:
        self.values.append(val)
        if not self.min_values or val < self.min_values[-1][0]:
            self.min_values.append([val, 1])
        elif val == self.min_values[-1][0]:
            self.min_values[-1][1] += 1
    
    def pop(self) -> int:
        val = self.values.pop()
        if val == self.min_values[-1][0]:
            self.min_values[-1][1] -= 1
            if self.min_values[-1][1] == 0:
                self.min_values.pop()
                
    def top(self) -> int:
        return self.values[-1] if self.values else None
    
    def get_min(self) -> int:
        return self.min_values[-1][0] if self.min_values else None
        
        
        
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(100)
    minStack.push(2000)
    minStack.push(4000)
    minStack.push(8000)
    minStack.push(10)
    minStack.push(80000)
    minStack.push(10)
    print(minStack.get_min())
    print(minStack.top())
    minStack.pop()
    print(minStack.get_min())
    print(minStack.top())
    minStack.pop()
    print(minStack.get_min())
    print(minStack.top())
    