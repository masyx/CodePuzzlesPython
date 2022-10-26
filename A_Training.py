from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='->')
            temp = temp.next
        print()


def removeDuplicatesFromLinkedList_2(head):
    previous = head
    current = head.next
    while current:
        if current.value == previous.value:
            previous.next = current.next
            current = previous.next
            continue
        current = current.next
        previous = previous.next
    return None


def removeDuplicatesFromLinkedList(head):
    current_node = head
    while current_node:
        next_node = current_node.next
        while next_node and next_node.value == current_node.value:
            next_node = next_node.next
        current_node.next = next_node
        current_node = next_node
    return head


def main():
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(1)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(2)

    removeDuplicatesFromLinkedList(head)
    head.print_list()


main()