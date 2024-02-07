# The operation on the stack: push, peek, pop, is_empty, stack_size

class MyStack:
    def __init__(self):
        self.stack_size = 0
        self.elements = []
        
    def is_empty(self):
        return self.stack_size == 0
    
    def push(self, element):
        self.stack_size += 1
        self.elements.append(element)
        
    def peek(self):
        if self.is_empty():
            return None
        return self.elements[-1]
    
    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.elements.pop()
    
    def __str__(self) -> str:
        # Represents the stack as a string
        return "Stack(bottom -> top): " + str(self.elements)
    
    @property
    def size(self):
        return self.stack_size
    