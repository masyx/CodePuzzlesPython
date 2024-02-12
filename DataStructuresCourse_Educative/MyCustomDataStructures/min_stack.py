class MinStack:
    def __init__(self):
        self.stack_size = 0
        self.elements = []
        self.min_val_indices = []

    def is_empty(self):
        return self.stack_size == 0
    
    def push(self, element):
        self.stack_size += 1
        self.elements.append(element)
        
        if self.stack_size == 1:
            self.min_val_indices.append(0)
        elif element < self.elements[self.min_val_indices[-1]]:
            self.min_val_indices.append(self.stack_size - 1)
        
    def peek(self):
        if self.is_empty():
            return None
        return self.elements[-1]
    
    def pop(self):
        if self.is_empty():
            return None
        
        if self.stack_size - 1 == self.min_val_indices[-1]:
            self.min_val_indices.pop()
        
        self.stack_size -= 1
        return self.elements.pop()
    
    def min(self):
        if self.min_val_indices:
            return self.elements[self.min_val_indices[-1]]
    
    def __str__(self) -> str:
        # Represents the stack as a string
        return "Stack(bottom -> top): " + str(self.elements)
    
    
if __name__ == "__main__":
    empty_stack = MinStack()
    print(f"min value in empty_stack is: {empty_stack.min()}")
    
    ## min_stack = [9, 3, 1, 4, 2, 5]
    ## min_stack.min()
    stack = MinStack()
    stack.push(9)
    print(stack)
    print(f"min value in the stack: {stack.min()}")
    stack.push(3)
    print(stack)
    print(f"min value in the stack: {stack.min()}")
    stack.push(1)
    print(stack)
    print(f"min value in the stack: {stack.min()}")
    stack.push(4)
    print(stack)
    print(f"min value in the stack: {stack.min()}")
    stack.push(2)
    print(stack)
    print(f"min value in the stack: {stack.min()}")
    stack.push(5)
    print(stack)
    print(f"min value in the stack: {stack.min()}")
    stack.push(-99)
    print(stack)
    print(f"min value in the stack: {stack.min()}")
    
    # popping the elements
    
    stack.pop()
    print(stack)
    print(f"min value in the stack: {stack.min()}")
    stack.pop()
    print(stack)
    print(f"min value in the stack: {stack.min()}")
    stack.pop()
    print(stack)
    print(f"min value in the stack: {stack.min()}")
    stack.pop()
    print(stack)
    print(f"min value in the stack: {stack.min()}")
    stack.pop()
    print(stack)
    print(f"min value in the stack: {stack.min()}")
