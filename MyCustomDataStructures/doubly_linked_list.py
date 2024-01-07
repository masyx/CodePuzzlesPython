from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def get_head(self):
        return self.head if self.head else None
        
    def is_empty(self):
        return self.head is None

    def get_head(self):
        return self.head
    
    def is_empty(self):
        return self.size == 0
        
    def append(self, element):
        self.tail.next = Node(element)
        self.tail = self.tail.next