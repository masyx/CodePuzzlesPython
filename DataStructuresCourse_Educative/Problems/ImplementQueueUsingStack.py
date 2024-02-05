import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from my_stack import MyStack

class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()


    def enqueue(self, value):
        self.main_stack.push(value)
        print(f"Enqueued element {value}")
        return True


    def dequeue_brute_force_my(self):
        if self.main_stack.is_empty():
            return None
        
        returnElement = self.main_stack.elements[0]
        
        updated_main_stack = []
        
        for i in range(1, self.main_stack.size):
            updated_main_stack.append(self.main_stack.elements[i])
        
        self.main_stack.elements = updated_main_stack
        self.main_stack.stack_size = len(self.main_stack.elements)
        return returnElement
    
    def dequeue(self):
        if self.temp_stack.is_empty() and self.main_stack.is_empty():
            print("Queue is empty")
            return None
        
        if self.temp_stack.is_empty():
            while not self.main_stack.is_empty():
                self.temp_stack.push(self.main_stack.pop())

        front = self.temp_stack.pop()
        print(f"Dequeued element {front}")
        return front

        
        
    
    
if __name__ == "__main__":
    newQueue = NewQueue()
    newQueue.enqueue(1)
    newQueue.enqueue(2)
    newQueue.enqueue(3)
    
    print(newQueue.main_stack.elements)
    
    newQueue.dequeue()
    newQueue.enqueue(4)
    newQueue.dequeue()
    newQueue.dequeue()
    newQueue.dequeue()
    newQueue.dequeue()