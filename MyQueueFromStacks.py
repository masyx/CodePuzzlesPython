'''
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) - Pushes element x to the back of the queue.
int pop() - Removes the element from the front of the queue and returns it.
int peek() - Returns the element at the front of the queue.
boolean empty() - Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
'''


class MyQueue_my_og:
    def __init__(self):
        self.pushing = []
        self.popping = []
    
    def push(self, value):
        self.pushing.append(value)
        
    def pop(self):
        if self.popping:
            return self.popping.pop()
        else:
            while self.pushing:
                self.popping.append(self.pushing.pop())
            return self.popping.pop()
        
    def peek(self):
        if self.popping:
            return self.popping[-1]
        elif self.pushing:
            return self.pushing[0]
        else:
            return None
    
    def empty(self):
        push_empty = len(self.pushing) == 0
        pop_empty = len(self.popping) == 0
        return push_empty and pop_empty
    
class MyQueue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        
    def push(self, value):
        self.push_stack.append(value)
        
    def pop(self):
        self._transfer_if_needed()
        return self.pop_stack.pop()
    
    def peek(self):
        self._transfer_if_needed()
        return self.pop_stack[-1]
    
    def empty(self):
        return not self.push_stack and not self.pop_stack
    
    def _transfer_if_needed(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            
            
# push_stack [1x, 2x, 3]
# pop_stack [2, 1x]
if __name__ == "__main__":
    queue = MyQueue_my_og()
    queue.push(1)
    queue.push(8)
    print(queue.pop())
    queue.push(3)
    print(queue.peek())
    print(queue.pop())
    queue.push(5)
    print(queue.pop())


    print(queue.empty())
    print()
    
    queue = MyQueue()
    queue.push(1)
    queue.push(8)
    print(queue.pop())
    queue.push(3)
    print(queue.peek())
    print(queue.pop())
    queue.push(5)
    print(queue.pop())


    print(queue.empty())