class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def is_palindromic_linked_list(head):
    middle = find_middle_node(head)
    reversed_second_half = reverse_linked_list(middle)
    
    while head and reversed_second_half:
        if head.value != reversed_second_half.value:
            return False
        head = head.next
        reversed_second_half = reversed_second_half.next
    return True

def find_middle_node(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse_linked_list(head):
    current = head
    previous = None
    while current:
        follow = current.next
        current.next = previous
        previous = current
        current = follow
    return previous
    
def main():
    head = Node(2)
    head.next = Node(1)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    #print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    #head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

if __name__ == "__main__":
    main()