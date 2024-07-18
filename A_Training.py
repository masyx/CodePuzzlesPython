class MyQueue:
    def __init__(self) -> None:
        self.stack_push = []
        self.stack_pop = []
    
    def push(self, val):
        self.stack_push.append(val)
        
    def peek(self):
        self.move_elements()
        return self.stack_pop[-1]
    
    def pop(self):
        self.move_elements()
        return self.stack_pop.pop()
    
    def move_elements(self):
        while self.stack_push:
            self.stack_pop.append(self.stack_push.pop())
    
    def empty(self):
        if not self.stack_pop and not self.stack_push:
            return True

if __name__ == "__main__":
    nums = [1,2,5,5,5,8,6]
    print(find_max_sliding_window(nums, 4))