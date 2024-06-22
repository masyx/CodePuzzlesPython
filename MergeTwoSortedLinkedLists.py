class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1: return list2
    if not list2: return list1
    
    result = ListNode()
    while list1:
        current = ListNode()
        if list1.val < list2.val:
            current.val = list1.val
            current.next = ListNode(list2.val)
        else:
            current.val = list2.val
            current.next = ListNode(list1.val)
        result = current
        result = result.next
        list1 = list1.next
        list2 = list2.next
    current

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    
    current = mergeTwoLists(list1, list2)
    
    while current:
        print(f" -> {current.next}")
        current = current.next
