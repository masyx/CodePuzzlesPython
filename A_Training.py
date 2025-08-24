from typing import Optional


class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        

# l1: 1 -> 3
# l2: 0 -> 5
# l3: 
class Solution:
    def reorderList(self, head: Optional[ListNode]):
        if not head or not head.next:
            return

        # 1. Find the node BEFORE the middle of the list
        slow, fast = head, head
        pre_slow = None
        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
            
        # 2. Sever the list into two halves
        pre_slow.next = None
        
        # 3. Reverse the second half (l2)
        l2 = None # Head of the reversed second list
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = l2
            l2 = curr
            curr = next_node
        
        # 4. Merge the two lists
        l1 = head
        while l2:
            # Store the next nodes before re-wiring
            l1_next = l1.next
            l2_next = l2.next
            
            # Weave l2 node after l1 node
            l1.next = l2
            
            # This is the crucial fix: If l1 has no more nodes,
            # the rest of l2 is already correctly attached as the tail.
            # We can stop here.
            if l1_next is None:
                break
            
            # Continue the weave
            l2.next = l1_next
            
            # Advance to the next pair of nodes
            l1 = l1_next
            l2 = l2_next    
def main():
    # original: 1 2 3 4 5
    # result:   1 5 2 4 3
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    
    l2 = ListNode(0)
    l2.next = ListNode(5)
    
    sol = Solution()
    #head = sol.mergeTwoListsRec(l1, l2)
    head = l1
    sol.reorderList(head)
    
    while head:
        print(head.val)
        head = head.next



if __name__ == "__main__":
    main()
        