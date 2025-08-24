"""143. Reorder List
Medium

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 100

"""


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
    # 1-2-3-4-5
    def reorderList(self, head: Optional[ListNode]) -> None:
        # STEP1: Find the middle of the list using slow/fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next # stops at 3
            fast = fast.next.next
        # At this point: slow = end of first half(stops at 3)
        
        # STEP2: Reverse the second half of the list
        second = slow.next # Start of the second ll
        slow.next = previous = None # Cut the list in half
        curr = second
        while curr:
            next_to_process = curr.next
            curr.next = previous
            previous = curr
            curr = next_to_process
        # Now: 'head' is the start of the first list, 
        # 'previous' is the head of the second reversed half 
        
        # STEP3: Merge two halves together  
        first = head # first ll
        second = previous # second ll
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 
        # tmp1:       V
        # ll1:    1-2-3-None
        # tmp2:        V
        # ll2:    5-4-None
        # 
        # new ll: 1-5-2-4-3
    
def main():
    ll1 = LinkedList(1)
    ll1.insert_at_end(2)
    ll1.insert_at_end(3)
    ll1.insert_at_end(4)
    ll1.insert_at_end(5)
    print(ll1)
    # ll.reverse()
    # print(ll)
    
    sol = Solution()
    
    sol.reorderList(ll1.head)
    print(ll1)

    
    
if __name__ == "__main__":
    main()
        