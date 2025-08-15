class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
class Solution:
    # 1 2 4 5 6  target = 2
    def removeNode(self, head, target):
        if head.val == target:
            return head.next
        
        prev = None
        curr = head
        
        while curr:
            if curr.val == target:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        return head
    
    
def main():
    sol = Solution()
    ll = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
    head = sol.removeNode(ll, 2)
    
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
    
    
    
if __name__ == "__main__":
    main()