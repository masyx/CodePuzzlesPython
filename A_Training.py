class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

# O(n) time | O(n) space
def reverse(head):
    new_next = None
    current = head
    while current:
        traverse_next = current.next
        current.next = new_next
        new_next = current
        current = traverse_next
    return new_next

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    
    new_head = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    new_head.print_list()
    
    reverse(new_head)
    print("Nodes of original LinkedList are: ", end='')
    head.print_list()


main()