import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')

from node import Node
from linked_list import LinkedList
        
        
def remove_nth_last_node_brute_force(head, n):
    length = 1
    curr_node = head
    while curr_node.next:
        length += 1
        curr_node = curr_node.next

    if length == n:
        return head.next
    
    m = length - n
    previous_node = head
    curr_node = head.next

    for i in range(m - 1):
        previous_node = curr_node
        curr_node = curr_node.next

    if n == 1:
        previous_node.next = None
    else:
        previous_node.next = curr_node.next

    return head

def remove_nth_last_node(head, n):
    first, second = head, head
    previous = None
    
    for _ in range(n):
        first = first.next
    
    if not first:
        return head.next
        
    while first.next:
        first = first.next
        previous = second
        second = second.next
    
    previous.next = second.next
    
    return head

def remove_nth_last_node_best(head, n):
    # Create a dummy node to handle edge cases where the head needs to be removed
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy
    
    # Move the first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until the first pointer reaches the end
    while first is not None:
        first = first.next
        second = second.next
    
    # Remove the nth last node
    second.next = second.next.next
    
    return dummy.next



def main():
    # [5, 7, 9, 12]
    ll = LinkedList()
    ll.insert_at_tail(5)
    ll.insert_at_tail(7)
    ll.insert_at_tail(9)
    ll.insert_at_tail(12)
    
    print(ll)
    remove_nth_last_node_best(ll.get_head(), 2)
    print(ll)
    
    

if __name__ == "__main__":
    main()