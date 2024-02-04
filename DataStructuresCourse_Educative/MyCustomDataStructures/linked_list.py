from node import Node

class LinkedList:
    def __init__(self):
        self.head_node = None
        
    def __str__(self):
        curr = self.head_node
        linkedList = []
        while curr:
            linkedList.append(str(curr.data))
            curr = curr.next
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
            if current_node.data == value:
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
        return slow.data
    
    def length(self):
        currNode = self.head_node
        
        counter = 0
        while currNode:
            counter += 1
            currNode = currNode.next
        return counter



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
        if current_node.data == value:
            return True
    return False

# O(n) time | O(n) space
def search_recursive(lst: LinkedList, value):
    def search(node, value):
        if not node:
            return False
        elif node.data == value:
            return True
        return search(node.next, value)
    
    return search(lst.get_head(), value)

def delete(lst: LinkedList, value):
    currentNode = lst.get_head()
    
    if not currentNode:
        return False
    
    if currentNode.data == value:
        lst.head_node = currentNode.next
        return True
    
    while currentNode.next:
        if currentNode.next.data == value:
            currentNode.next = currentNode.next.next
            return True
        currentNode = currentNode.next
        
    return False


def length(lst: LinkedList):
    currNode = lst.get_head()
    counter = 0
    while currNode:
        counter += 1
        currNode = currNode.next
    return counter

def find_mid(lst: LinkedList):
    if not lst.head_node:
        return None
    slow = lst.head_node
    fast = lst.head_node
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

def find_mid_naive(lst: LinkedList):
    length = lst.length()
    
    if length % 2 == 0:
        middle_index = length//2 - 1
    else:
        middle_index = (length - 1)//2
    node = lst.get_head()
    
    for i in range(middle_index):
        node = node.next
    return node.data

def remove_duplicates(lst: LinkedList):
    if not lst.get_head():
        return None
    curr_node = lst.head_node
    visited = {curr_node.data}
    while curr_node.next:
        if curr_node.next.data in visited:
            curr_node.next = curr_node.next.next
        else:
            visited.add(curr_node.next.data)
            curr_node = curr_node.next
    return lst

def union(lst1: LinkedList, lst2):
    result = LinkedList()
    union_set = set()
    tail = None
    def add_elements_to_set(linked_list, target_set):
        curr = linked_list.get_head()
        while curr:
            target_set.add(curr.data)
            curr = curr.next
    
    add_elements_to_set(lst1, union_set)
    add_elements_to_set(lst2, union_set)
    
    for element in union_set:
        new_node = Node(element)
        if tail:
            tail.next = new_node
        else:
            result.head_node = new_node
        tail = new_node

    return result

def intersection(lst1: LinkedList, lst2):
    result = LinkedList()
    visited = set()
    curr = lst1.head_node
    while curr:
        visited.add(curr.data)
        curr = curr.next
    
    curr_lst2 = lst2.head_node
    tail = None
    while curr_lst2:
        new_node = Node(curr_lst2.data)
        if curr_lst2.data in visited:
            if tail:
                tail.next = new_node
            else:
                result.head_node = new_node
            tail = new_node 
        curr_lst2 = curr_lst2.next
    return remove_duplicates(result)

def find_nth_from_end(lst: LinkedList, n):
    if not lst.get_head():
        return -1
    
    length = lst.length()
    node_number_to_return = length - n
    if node_number_to_return < 0:
        return -1
    curr = lst.get_head()
    
    for _ in range(node_number_to_return):
        curr = curr.next
    return curr.data

def find_nth_from_end_2(lst: LinkedList, n):
    if not lst.head_node:
        return -1
    
    end_node = nth_node = lst.get_head()
    
    for _ in range(n):
        if end_node is None:
            return - 1
        end_node = end_node.next
        
    while end_node:
        end_node = end_node.next
        nth_node = nth_node.next
    return nth_node.data