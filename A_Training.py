class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, curr: Node = None):
        self.curr  = curr
        
    def __str__(self):
        curr = self.curr
        res = []
        while curr:
            res.append(str(curr.value))
            curr = curr.next
        return "->".join(res)
        
class Solution:
        def mergeTwoLists(self, list1, list2):
            if not list1 or not list2:
                return list2 if not list1 else list1
            
            curr = None
            if list1.value < list2.value:
                curr = list1
                list1 = list1.next
            else:
                curr = list2
                list2 = list2.next
            
            head = curr
            while list1 and list2:
                if list1.value < list2.value:
                    curr.next = list1
                    curr = curr.next
                    list1 = list1.next
                else:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next
                    
            while list1:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            while list2:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            
            return head
                    
def main():
    ll = LinkedList()
    ll.curr = Node(1)
    ll.curr.next = Node(3)
    
    ll_2 = LinkedList()
    ll_2.curr = Node(2)
    ll_2.curr.next = Node(4)
    
    solution = Solution()
    print(ll)
    ll.curr = solution.mergeTwoLists(ll.curr, ll_2.curr)
    print(ll)
    
    
     
if __name__ == "__main__":
    main()
        