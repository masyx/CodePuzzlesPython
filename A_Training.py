class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self, head, next=None):
        self.length = 0
        self.head = Node(head, next)
        
    @classmethod
    def from_node(cls, node):
        return cls(node.value, node.next)
        
    def insert_at_tail(self, value):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)
        
    def __str__(self) -> str:
        current = self.head
        visited = []
        while current:
            visited.append(str(current.value))
            current = current.next
        return " -> ".join(visited)


def is_linkedList_palindrome(head):
    middle = find_middle_node(head)
    head_reversed = reverse_linkedList(middle)
    is_palindrome = is_linkedList_palindrome_helper(head, head_reversed)
    reverse_linkedList(head_reversed)
    return is_palindrome

# [1, 2, 3, 4] 
# slow: 1 2 3
# fast: 1 3 None

# [1, 2, 3, 2, 1] 
# slow: 1 2 3
# fast: 1 3 5
def find_middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse_linkedList(head):
    previous = None
    current = head
    while current:
        follow = current.next
        current.next = previous
        previous = current
        current = follow
    return previous

def is_linkedList_palindrome_helper(head_1, head_2):
    while head_1 and head_2:
        if head_1.value != head_2.value:
            return False
        head_1 = head_1.next
        head_2 = head_2.next
    return True



if __name__ == "__main__":
    ll = LinkedList(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(4)
    ll.insert_at_tail(5)
    ll.insert_at_tail(99)
    ll.insert_at_tail(2)
    ll.insert_at_tail(1)
    
    print(f"Is LinkedList [{ll}] a palindrome - {'yes' if is_linkedList_palindrome(ll.head) else 'no'}")
