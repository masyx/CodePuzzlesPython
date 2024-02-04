# Generate Binary Numbers from 1 to n using a Queue
"""  
Implement a function find_bin(n) which will generate binary numbers from 
1 till n in the form of a string using a queue."""

import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from my_queue import MyQueue


def generate_binary_numbers_my(numbers):
    if numbers == 0:
        return None
    
    result = ['1']
    queue = MyQueue()
    queue.enqueue('1')
    
    while len(result) != numbers and queue:
            current = queue.dequeue()
            result.append(current + '0')
            queue.enqueue(current + '0')
            
            if len(result) != numbers:
                result.append(current + '1')
                queue.enqueue(current + '1')
    return result


def generate_binary_numbers(numbers):
    if numbers == 0:
        return []
    
    result = []
    queue = MyQueue()
    queue.enqueue('1')
    
    for _ in range(numbers):
        current = queue.dequeue()
        result.append(current)
        queue.enqueue(current + '0')
        queue.enqueue(current + '1')
        
    return result

if __name__ == "__main__" :
    result = generate_binary_numbers(20)
    print(result)