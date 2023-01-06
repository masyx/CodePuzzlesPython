class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head_node = None
        
    def __str__(self):
        head = self.get_head()
        # linkedList = ""
        # while head:
        #     linkedList += f"{head.value} -> "
        #     #linkedList.join(head) 
        #     head = head.next
        linkedList = []
        while head:
            linkedList.append(str(head.value))
            head = head.next
        return " -> ".join(linkedList)
        
    def get_head(self):
        return self.head_node
    
    def is_empty(self):
        if not self.head_node:
            return True
        return False
    
    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head_node
        self.head_node = new_node
        return self.head_node
    
    def insert_at_tail(self, value):
        current_node = self.get_head()
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(value)


@staticmethod
def insert_at_tail(lst, value):
    current_node = lst.get_head()
    while current_node.next:
        current_node = current_node.next
    current_node.next = Node(value)
