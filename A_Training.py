from typing import Optional


class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        

# l1: 1 -> 3
# l2: 0 -> 5
# l3: 
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 or list2
            
        return dummy.next
    
    def mergeTwoListsRec(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoListsRec(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRec(l1, l2.next)
            return l2
            
    
def main():
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l2 = ListNode(0)
    l2.next = ListNode(5)
    
    sol = Solution()
    head = sol.mergeTwoListsRec(l1, l2)
    
    while head:
        print(head.val)
        head = head.next



if __name__ == "__main__":
    main()
        