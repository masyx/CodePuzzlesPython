class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, head: Node = None):
        self.head  = head
        
    def __str__(self):
        curr = self.head
        res = []
        while curr:
            res.append(str(curr.value))
            curr = curr.next
        return "->".join(res)
        
class Solution:
    def reverse_list(self, head):
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
            
            
def main():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    
    solution = Solution()
    print(ll)
    ll.head = solution.reverse_list(ll.head)
    print(ll)
    
    
     
if __name__ == "__main__":
    main()