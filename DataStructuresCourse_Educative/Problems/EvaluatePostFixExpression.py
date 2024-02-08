import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from my_stack import MyStack

def evaluate_post_fix(expression: MyStack):
    operands = []
    for i in range(expression):
        while expression[i] is str:
            