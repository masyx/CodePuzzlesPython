import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')

from node import Node
from linked_list import LinkedList
        
        
def remove_nth_last_node(head, n):
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


def main():
    # [5, 7, 9, 12]
    ll = LinkedList()
    ll.insert_at_tail(5)
    ll.insert_at_tail(7)
    ll.insert_at_tail(9)
    ll.insert_at_tail(12)
    
    print(ll)
    remove_nth_last_node(ll.get_head(), 2)
    print(ll)
    
    

if __name__ == "__main__":
    main()