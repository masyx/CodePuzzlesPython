from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self, head):
        self.head = ListNode(head)
        
    def insert_at_end(self, val):
        curr_node = self.head
        previous = None
        while curr_node:
            previous = curr_node
            curr_node = curr_node.next
        previous.next = ListNode(val)
    
    def __str__(self):
        curr = self.head
        res = []
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        return ",".join(res)
    
    def reverse(self):
        curr = self.head
        previous = None
        while curr:
            next_to_process = curr.next
            curr.next = previous
            previous = curr
            curr = next_to_process
        self.head = previous
                
class Solution:
    # O(n) time | O(n) space
    def reorderListRecursion(self, head: Optional[ListNode]) -> None:

        def rec(root: ListNode, cur: ListNode) -> ListNode:
            if not cur:
                return root

            root = rec(root, cur.next)
            if not root:
                return None

            tmp = None
            if root == cur or root.next == cur:
                cur.next = None
            else:
                tmp = root.next
                root.next = cur
                cur.next = tmp

            return tmp

        head = rec(head, head.next)
        
    # O(n) time | O(1) space
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    
    def mergeTwoListsIterative(self, list1, list2):
        pre_head = ListNode(-1)
        tail = pre_head # will point to the last node of the merged list
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return pre_head.next.next
        
def main():
    ll1 = LinkedList(1)
    ll1.insert_at_end(2)
    # ll1.insert_at_end(3)
    # ll1.insert_at_end(4)
    # ll1.insert_at_end(5)
    print(ll1)
    
    sol = Solution()
    ll2 = LinkedList(3) 
    print(sol.mergeTwoListsIterative(ll1.head, ll2.head))
    
    
if __name__ == "__main__":
    main()
        