'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together 
the nodes of the first two lists. Return the head of the merged linked list.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n + m) time | O(n + m) space
def mergeTwoListsRecursive(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1.val < l2.val:
        l1.next = mergeTwoListsRecursive(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoListsRecursive(l1, l2.next)
        return l2

# O(n + m) time | O(1) space
def mergeTwoListsIterative(l1, l2):
    pre_head = ListNode(-1)
    current = pre_head
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return pre_head.next
    
if __name__ == "__main__":
    list1 = ListNode(0)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    
    # head  = mergeTwoListsRecursive(list1, list2)
    # curr = head
    # while curr:
    #     print(curr.val, "->", end=" ")
    #     curr = curr.next
    # print()
        
        
    current = mergeTwoListsIterative(list1, list2)
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))
