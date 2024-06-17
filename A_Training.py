class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, head):
        self.length = 0
        self.head = Node(head)
        
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


def get_middle_node(head: Node):
    if head is None:
        return -1
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    ll = LinkedList(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_tail(4)
    ll.insert_at_tail(5)
    print(ll)
    print(f"Middle of the linked list is node: {get_middle_node(ll.head).value}")
    ll.insert_at_tail(6)
    print("Added node 6")
    print(f"Middle of the linked list is node: {get_middle_node(ll.head).value}")
