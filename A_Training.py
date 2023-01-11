import linked_list
from linked_list import Node
from linked_list import LinkedList

def main():
    ll = LinkedList()
    ll.head_node = Node(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_tail(4)
    ll.insert_at_tail(5)
    ll.insert_at_tail(6)
    ll.insert_at_tail(7)

    print(ll.middle())
    
    
    
if __name__ == "__main__":
    main()