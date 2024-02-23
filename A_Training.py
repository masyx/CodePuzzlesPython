from collections import deque

class Node:
    def __inti__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        
    def add_node(self, value):
        new_node = Node(value)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        
    def add_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        

class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adjacency_list = [LinkedList() for _ in range(vertices)]

if __name__ == "__main__":
