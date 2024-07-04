class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def printLinkedList(head: Node):
    current = head
    result = []
    seen = set()
    while current:
        if current not in seen:
            result.append(str(current.val))
            seen.add(current)
            current = current.next
        else:
            break
    return " -> ".join(result)

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(99)
    head.next.next.next = head
    
    print(f"Does LinkedList [{printLinkedList(head)}] has cycle: {'Yes' if hasCycle(head) else 'No'}")