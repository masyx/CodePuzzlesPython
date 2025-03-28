class MinStack1:

    def __init__(self):
        self.stack = []
        self.min_values = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_values or val <= self.min_values[-1]:
            self.min_values.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_values[-1]:
                self.min_values.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_values:
            return self.min_values[-1]
        return None


class MinStack:
    def __init__(self):
        self.values = []
        # [[1,1], [0, 1]]
        self.min_values = []
        
    def push(self, val: int) -> None:
        self.values.append(val)
        if not self.min_values or val < self.min_values[-1][0]:
            self.min_values.append([val, 1])
        elif val == self.min_values[-1][0]:
            self.min_values[-1][1] += 1
    
    def pop(self) -> None:
        if self.values:
            val = self.values.pop()
            if val == self.min_values[-1][0]:
                self.min_values[-1][1] -= 1
                if self.min_values[-1][1] == 0:
                    self.min_values.pop()
    
    def top(self) -> int:
        if self.values:
            return self.values[-1]
    
    def getMin(self) -> int:
        if self.min_values:
            return self.min_values[-1][0]
  
    
def main():
    stack = MinStack()
    # stack.push(5)
    # stack.push(6)
    # stack.push(-1)
    # stack.push(8)
    # stack.push(-88)
    # print(stack.getMin())
    # print(stack.top())
    # print(stack.pop())
    # print(stack.top())
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    print(stack.getMin())
    #["MinStack","push","push","push","getMin","pop","getMin"]
    #[[],[0],[1],[0],[],[],[]]
    stack.push(0)
    stack.push(1)
    stack.push(0)
    stack.push(0)

    
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())
    stack.push(-1)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.top()

    
     
if __name__ == "__main__":
    main()