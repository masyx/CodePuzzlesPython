class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result

def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value
        
        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")

def reverse_linked_list(slow_ptr):
    reverse = None
    while slow_ptr is not None:
        next = slow_ptr.next
        slow_ptr.next = reverse
        reverse = slow_ptr
        slow_ptr = next
    return reverse


### PROGRAM START
# Check palindrome in linked_list
def palindrome(head):
    # Initialize variables with head
    slow = head
    fast = head
    revert_data = None
    mid_node = head

    # Traverse linked_list through fast and slow
    # pointers to get the middle node
    while fast and fast.next:
        mid_node = slow
        slow = slow.next
        fast = fast.next.next

    # Fast pointer of odd linked list will point to last node
    # of linked list but it will point to NULL for even linked list
    saved_odd_mid_node = None
    if fast:
        saved_odd_mid_node = slow
        slow = slow.next

    # It will skip the first half
    mid_node.next = None
    # Pass middle node as a head to reverse function
    # to revert the next half of linked_list
    revert_data = reverse_linked_list(slow)
    # Pass second half reverted data to compare_two_halves
    # function to check the palindrome property
    check = False
    check = compare_two_halves(head, revert_data)
    # Revert second half back to the original linked list
    revert_data = reverse_linked_list(revert_data)

    # Connect both halves
    # If linked list was of odd sized, connect the middle node
    # first which was skipped while reverting the second half
    if saved_odd_mid_node:
        mid_node.next = saved_odd_mid_node
        saved_odd_mid_node.next = revert_data
    else:
        mid_node.next = revert_data

    # Return true if there's only one node
    # or both are pointing to NULL
    if head is None or revert_data is None:
        return True
    if check:
        return True
    return False


def compare_two_halves(first_half, second_half):
    check = False
    while first_half is not None and second_half is not None:
        if first_half.data != second_half.data:
            check = False
            break
        else:
            check = True
        first_half = first_half.next
        second_half = second_half.next
    return check


def main():
    input = (
                [2, 4, 6, 4, 2],
                [0, 3, 5, 5, 0],
                [9, 7, 4, 4, 7, 9],
                [5, 4, 7, 9, 4, 5],
                [5, 9, 8, 3, 8, 9, 5],
            )
    j = 1

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(j, ".\tLinked List:", end=" ")
        print_list_with_forward_arrow(input_linked_list.head)
        head = input_linked_list.head
        print("\n\tIs it a palindrome?", "Yes" if palindrome(head) else "No")
        j += 1
        print("-"*100, "\n")


if __name__ == "__main__":
    main()
	