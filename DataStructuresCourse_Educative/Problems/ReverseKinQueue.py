''' Implement the function reverseK(queue, k) which takes a queue and a number “k” as input
    and reverses the first “k” elements of the queue. An illustration is also provided for your understanding.'''
    
import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from my_queue import MyQueue

# O(n) time | O(n) space, but it is up for a discussion, I am reallocating the memory here
# so it is not extra memory. So we can argue that this is actually O(1) space
def reverseK_myFirst(queue: MyQueue, k):
    if queue is None or k > queue.size() or k < 0:
        return None
        
    stack = []
    for _ in range(k):
        stack.append(queue.dequeue())
    
    result_queue = MyQueue()
    while stack:
        result_queue.enqueue(stack.pop())
        
    while queue.size() != 0:
        result_queue.enqueue(queue.dequeue())
        
    return result_queue

def reverseK(queue: MyQueue, k):
    if queue is None or k > queue.size() or k < 0:
        return None
        
    stack = []
    for _ in range(k):
        stack.append(queue.dequeue())
    
    while stack:
        queue.enqueue(stack.pop())
        
    for _ in range(queue.size() - k):
        queue.enqueue(queue.dequeue())
        
    return queue


if __name__ == "__main__":
    
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    
    print(reverseK(queue, 2))