from linked_list import LinkedList
from linked_list import Node
from linked_list import insert_at_tail
from linked_list import search
from linked_list import search_recursive
from linked_list import delete

def main():
    arr = [6, 2, 99, 3, 9, 0]
    print(binarySearchRecursive(arr, 99))
    print(binarySearchIterative(arr, 99))
    
    
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
    delete(ll, 7)
    print(ll)
    
    delete(ll_2, 0)
    delete(ll_2, 0)
    print(ll_2)

    delete(LinkedList(), 0)
    
def binarySearchRecursive(list: list, value):
    if not list:
        return -1
    
    list.sort()
    
    return binarySearchHelper(list, 0, len(list) - 1, value)
    
def binarySearchHelper(list, l, r, value):
    if l > r:
        return -1
    
    middle = (l + r) // 2
    
    if list[middle] == value:
        return middle
    if value < list[middle]:
        return binarySearchHelper(list, 0, middle - 1, value)
    else:
        return binarySearchHelper(list, middle + 1, r, value)

def binarySearchIterative(list, target):
    if not list:
        return 
    
    list.sort()
    
    l = 0
    r = len(list) - 1
    
    while l <= r:
        middle = (l + r) // 2
        
        if list[middle] == target:
            return middle
        if target < list[middle]:
            r = middle - 1
        else:
            l = middle + 1


if __name__ == "__main__":
    main()