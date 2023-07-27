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
        return " -> ".join(linkedList) + " -> None" if linkedList else "LinkedList is empty"
        
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

# O(n) time | O(n) space
def search_recursive(lst: LinkedList, value):
    def search(node, value):
        if not node:
            return False
        elif node.value == value:
            return True
        return search(node.next, value)
    
    return search(lst.get_head(), value)

def delete(lst: LinkedList, value):
    currentNode = lst.get_head()
    
    if not currentNode:
        return False
    
    if currentNode.value == value:
        lst.head_node = currentNode.next
        return True
    
    while currentNode.next:
        if currentNode.next.value == value:
            currentNode.next = currentNode.next.next
            return True
        currentNode = currentNode.next
        
    return False