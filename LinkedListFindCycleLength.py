class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# Find where the slow pointer meets the fast pointer and loop again to find its length.
# O(n) time, O(n) space
def find_cycle_length(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_length = 1
            current = slow.next
            while current is not slow:
                cycle_length += 1
                current = current.next
            return cycle_length
    return 0


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))
    
    head.next.next.next.next.next.next = head.next.next.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()