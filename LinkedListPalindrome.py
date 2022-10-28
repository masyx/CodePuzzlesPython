class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    middle_node = find_middle_node(head)
    reversed_second_half_head = reverse_linked_list(middle_node)
    is_palindrome = compare_linked_lists(head, reversed_second_half_head)
    second_half = reverse_linked_list(reversed_second_half_head)
    return is_palindrome

def find_middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def compare_linked_lists(head_1, head_2):
    while head_1 and head_2:
        if head_1.value != head_2.value:
            return False
        head_1 = head_1.next
        head_2 = head_2.next
    return True

def reverse_linked_list(node):
    temp = None
    while node is not None:
        next = node.next
        node.next = temp
        temp = node
        node = next
    return temp

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(7)
    head.next.next.next.next = Node(4)

    #print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

if __name__ == "__main__":
    main()