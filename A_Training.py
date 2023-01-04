import LinkedList
from LinkedList import Node
from LinkedList import LinkedListClass

def main():
    ll = LinkedListClass()
    ll.head_node = Node(1)
    LinkedList.insert_at_tail(ll, Node(2))
    print()
    
    
if __name__ == "__main__":
    main()