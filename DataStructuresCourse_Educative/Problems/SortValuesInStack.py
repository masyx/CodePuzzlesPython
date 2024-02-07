import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from my_stack import MyStack

def sort_stack(stack: MyStack):
    helper_stack = MyStack()
    while not stack.is_empty():
        curr = stack.pop()
        while not helper_stack.is_empty() and curr > helper_stack.peek():
            stack.push(helper_stack.pop())
        helper_stack.push(curr)
    return helper_stack


if __name__ == "__main__":
    stack = MyStack()
    # stack.push(-555)
    stack.push(9)
    stack.push(0)
    stack.push(32)
    stack.push(5)
    stack.push(5)
    stack.push(99)
    stack.push(-66)
    stack.push(0)
    stack.push(5)
    stack.push(999)
    stack.push(-66)
    stack.push(32)
    stack.push(8888)
    
    print(sort_stack(stack))