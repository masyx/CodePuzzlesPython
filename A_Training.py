from linked_list import LinkedList
from linked_list import Node
from linked_list import insert_at_tail
from linked_list import search
from linked_list import search_recursive
from linked_list import delete

def main():
    ll = LinkedList()
    ll.head_node = Node(8)
    ll.insert_at_head(7)
    ll.insert_at_head(6)
    ll.insert_at_head(5)
    insert_at_tail(ll, 9)
    
    ll_2 = LinkedList()
    insert_at_tail(ll_2, 0)
    
    ll_3 = LinkedList()
    ll_3.insert_at_tail(1)

    print(ll.search(9))
    print(search_recursive(ll, 7))
    
    empty_ll = LinkedList()
    print(search(empty_ll, 7))
    
    ll.delete_at_head()
    print(ll)
    delete(ll, 8)
    print(ll)
    delete(ll, 9)
    print(ll)
    delete(ll, 6)
    print(ll)
    
    delete(ll_2, 0)
    delete(ll_2, 0)
    print(ll_2)

    delete(LinkedList(), 0)
    
if __name__ == "__main__":
    main()