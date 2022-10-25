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

# O(n) time | O(1) space
def find_cycle_start_2(head):
    cycle_length = find_cycle_length(head)
    slow = fast = head
    if cycle_length:
        for _ in range(cycle_length):
            fast = fast.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow
    return None

def find_cycle_length(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            current = slow
            cycle_length = 0
            while True:
                current = current.next
                cycle_length += 1
                if slow == current:
                    return cycle_length
    return 0

# O(n) time | O(1) space        
def find_cycle_start(head):
    # slow_ptr = fast_ptr = head
    # while fast_ptr and fast_ptr.next:
    #     slow_ptr = slow_ptr.next
    #     fast_ptr = fast_ptr.next.next
    #     if slow_ptr is fast_ptr:
    #         break
    # while True:
    #     slow_ptr = slow_ptr.next
    #     fast_ptr = fast_ptr.next.next
    #     if slow_ptr is fast_ptr:
    #         break
    slow_ptr = head.next
    fast_ptr = head.next.next
    while slow_ptr is not fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    slow_ptr = head
    while slow_ptr is not fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    return fast_ptr

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