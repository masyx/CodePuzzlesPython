class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head_node = None
        
    def __str__(self):
        head = self.head_node
        linkedList = []
        while head:
            linkedList.append(str(head.value))
            head = head.next
        return " -> ".join(linkedList) + " -> None"
        
    def get_head(self):
        return self.head_node
    
    def is_empty(self):
        return self.head_node is None
    
    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head_node
        self.head_node = new_node
        return self.head_node
    
    def insert_at_tail(self, value):
        current_node = self.head_node
        if current_node is None:
            self.head_node = Node(value)
            return
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(value)
        
    def search(self, value):
        current_node = self.head_node
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
    
    def delete_at_head(self):
        if self.head_node:
            self.head_node = self.head_node.next

    def reverse(self):
        current = self.head_node
        new_next_node = None
        while current:
            next_to_traverse = current.next
            current.next = new_next_node
            new_next_node = current
            current = next_to_traverse
        self.head_node = new_next_node
        
    def middle(self):
        slow = fast = self.head_node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value



#@staticmethod If I want I can have this decorator but I don't have to
# Without decorator this is module-level function
def insert_at_tail(lst, value):
    current_node = lst.get_head()
    if not current_node:
        lst.head_node = Node(value)
        return
    while current_node.next:
        current_node = current_node.next
    current_node.next = Node(value)

# O(n) time | O(1) space
def search(lst: LinkedList, value):
    current_node = lst.head_node
    while current_node:
        if current_node.value == value:
            return True
    return False

# O(n) time | O(1) space
def search_recursive():
    pass

def delete(lst, value):
    current = lst.head_node
    if current and current.value == value:
        lst.head_node = lst.head_node.next
        return True
    while current and current.next:
        if current.next.value == value:
            current.next = current.next.next
            return True
        current = current.next
    return False