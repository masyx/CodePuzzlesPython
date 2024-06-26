class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self, head, next=None):
        self.length = 0
        self.head = Node(head, next)
        
    @classmethod
    def from_node(cls, node: Node):
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


def get_middle_node(head: Node):
    pass

def merge_linked_lists(lst1: Node, lst2: Node):
    if lst1 is None:
        return lst2
    if lst2 is None:
        return lst1
    if lst1.value < lst2.value:
        lst1.next = merge_linked_lists(lst1.next, lst2)
        return lst1
    else:
        lst2.next = merge_linked_lists(lst1, lst2.next)
        return lst2

if __name__ == "__main__":
    ll = LinkedList(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(4)
    ll.insert_at_tail(10)
    print(ll)
    # print(f"Middle of the linked list is node: {get_middle_node(ll.head).value}")
    # ll.insert_at_tail(6)
    # print("Added node 6")
    # print(f"Middle of the linked list is node: {get_middle_node(ll.head).value}")
    
    ll_2 = LinkedList(0)
    ll_2.insert_at_tail(3)
    ll_2.insert_at_tail(7)
    print(ll_2)
    
    new_head = merge_linked_lists(ll.head, ll_2.head)
    
    ll_3 = LinkedList(new_head.value, new_head.next)
    print(ll_3)
    
    ll_4 = LinkedList.from_node(new_head)
    print(ll_4)