class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def add_at_tail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def __str__(self) -> str:
        result = []
        current = self.head
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)
    
    
def isPalindrome(head: Node) -> bool:
    middle_node = get_middle_node(head)
    reversed_head = reverse_linked_list(middle_node)
    isPal = isPalindromeHelper(head, reversed_head)
    reverse_linked_list(reversed_head)
    return isPal

def get_middle_node(head: Node):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 1 -> 2
def reverse_linked_list(head: Node):
    previous = None
    current = head
    while current:
        following = current.next # None
        current.next = previous # 1
        previous = current # 2
        current = following # None
    return previous
        
def isPalindromeHelper(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return True

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_at_tail(1)
    ll.add_at_tail(2)
    ll.add_at_tail(3)
    ll.add_at_tail(4)
    ll.add_at_tail(5)
    
    print(ll)
    print(isPalindrome(ll.head))
    
    
    ll_2 = LinkedList()
    ll_2.add_at_tail(1)
    ll_2.add_at_tail(2)
    ll_2.add_at_tail(2)
    ll_2.add_at_tail(1)
    
    print(ll_2)
    print(isPalindrome(ll_2.head))
    