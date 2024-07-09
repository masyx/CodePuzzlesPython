def merge_sorted_array(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    if arr1[0] < arr2[0]:
        res = merge_sorted_array(arr1[1:], arr2)
        merged_arr = [arr1[0]] + res
        return merged_arr
    else:
        res = merge_sorted_array(arr1, arr2[1:])
        merged_arr = [arr2[0]] + res
        return merged_arr
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def mergeTwoSortedLinkedLists(head1, head2):
    pre_head = Node(-1)
    current = pre_head
    
    while head1 and head2:
        if head1.value < head2.value:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
        
    current.next = head1 or head2
    return pre_head.next


if __name__ == "__main__":
    arr1 = [0, 2, 4]
    arr2 = [1, 3]
    print(merge_sorted_array(arr1, arr2))
    
    ll_1 = Node(0)
    ll_1.next = Node(2)
    
    ll_2 = Node(1)
    ll_2.next = Node(3)
    ll_2.next.next = Node(5)
    
    ll_res = mergeTwoSortedLinkedLists(ll_1, ll_2)
    
    ll_arr = []
    while ll_res:
        ll_arr.append(ll_res.value)
    
    print(" -> ".join(ll_arr))