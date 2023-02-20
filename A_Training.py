from linked_list import LinkedList
from linked_list import Node
from linked_list import insert_at_tail
from linked_list import search

def main():
    ll = LinkedList()
    ll.head_node = Node(8)
    ll.insert_at_head(7)
    ll.insert_at_head(6)
    
    insert_at_tail(ll, 9)
    
    ll_2 = LinkedList()
    insert_at_tail(ll_2, 0)
    
    ll_3 = LinkedList()
    ll_3.insert_at_tail(1)

    print(ll.search(9))
    
    empty_ll = LinkedList()
    print(search(empty_ll, 7))
    
if __name__ == "__main__":
    main()