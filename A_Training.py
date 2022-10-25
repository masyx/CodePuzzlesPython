from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
  
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    slow = fast = head
    cycle_length = find_cycle_length(head)
    if cycle_length > 0:
        for _ in range(cycle_length):
            fast = fast.next
        while True:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next
    return None

def find_cycle_length(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            current = slow.next
            cycle_length = 1
            while current is not slow:
                current = current.next
                cycle_length += 1
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
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()