from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def get_head(self):
        return self.head if self.head else None

    def get_tail(self):
        return self.tail if self.tail else None
    
    def is_empty(self):
        return self.head is None
    
    def insert_tail(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            
        self.length += 1
        return self.tail.data
    
    def remove_head(self):
        if self.is_empty():
            return None
        
        node_to_remove = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
            node_to_remove.next = None
        
        self.length -= 1
        return node_to_remove.data
    
    def __str__(self):
        val=""
        if(self.is_empty()):
            return ""
        temp = self.head
        val = "[" + str(temp.data) + ", "
        temp = temp.next_element

        while (temp.next_element):
            val = val + str(temp.data) + ", "
            temp = temp.next_element
        val = val + str(temp.data) + "]"
        return val

