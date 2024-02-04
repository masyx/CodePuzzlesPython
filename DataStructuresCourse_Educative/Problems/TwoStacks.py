class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.top1 = -1
        self.top2 = size

    # Insert Value in First Stack
    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.items[self.top1] = value
        else:
            print("Stack Overflow")

    # Insert Value in Second Stack
    def push2(self, value):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.items[self.top2] = value
        else:
            print("Stack Overflow")

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.top1 >= 0:
            popped_item = self.items[self.top1]
            self.items[self.top1] = None
            self.top1 -= 1
            return popped_item
        else:
            print("Stack Underflow in the stack1")
            return None

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.top2 < self.size:
            popped_item = self.items[self.top2]
            self.items[self.top2] = None
            self.top2 += 1
            return popped_item
        else:
            print("Stack Underflow in the stack2")
            return None
    

if __name__ == "__main__":
    stacks = TwoStacks(10)
    stacks.push1(1)
    stacks.push2(1)
    
    stacks.push1(2)
    stacks.push2(2)
    
    stacks.push1(3)
    stacks.push2(3)
    
    stacks.push1(4)
    stacks.push2(4)
    
    stacks.push1(5)
    stacks.push2(5)
    
    print(stacks.items)
    
    stacks.pop1()
    stacks.pop2()
    
    stacks.pop1()
    stacks.pop2()
    
    stacks.pop1()
    stacks.pop2()
    
    stacks.pop1()
    stacks.pop2()
    
    stacks.pop1()
    stacks.pop2()
    
    stacks.pop1()
    stacks.pop2()
    
    stacks.pop1()
    
    print(stacks.items)