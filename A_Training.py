class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, head):
        self.length = 0
        self.head = LinkedListNode(head)
        
    def insert_at_tail(self, value):
        current = self.head
        while current.next:
            current = current.next
        current.next = LinkedListNode(value)
        
    def __str__(self) -> str:
        current = self.head
        visited = []
        while current:
            visited.append(str(current.value))
            current = current.next
        return " -> ".join(visited)


def detect_cycle(head):
    if head is None:
        return False
    slow = fast = head
    while fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    ll = LinkedList(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_tail(4)
    ll.insert_at_tail(5)
    print(ll)
    print(f"Does the linked list has a cycle: {detect_cycle(ll.head)}")
    print("Added cycle from 5 to 1.")
    ll.head.next.next.next.next.next = ll.head
    #print(ll) infinite cycle, cannot print
    print(f"Does the linked list has a cycle: {detect_cycle(ll.head)}")
