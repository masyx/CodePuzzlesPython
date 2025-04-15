class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None
        
class LinkedList:
    def __init__(self, curr: Node = None):
        self.curr  = curr
        
    def __str__(self):
        curr = self.curr
        res = []
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        return "->".join(res)
        
class Solution:
        def mergeTwoLists(self, list1, list2):
            dummy = node = Node()
            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next
            
            node.next = list1 or list2
                
            return dummy.next
        # l1: 1           l2: 2
        def merge_two_list_recursion(self, list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val < list2.val:
                list1.next = self.merge_two_list_recursion(list1.next, list2)
                return list1
            else:
                list2.next = self.merge_two_list_recursion(list1, list2.next)
                return list2
                    
                
def main():
    ll = LinkedList()
    ll.curr = Node(1)
    ll.curr.next = Node(3)  
    
    ll_2 = LinkedList()
    ll_2.curr = Node(2)
    ll_2.curr.next = Node(4)
    
    solution = Solution()
    print(ll)
    print(ll_2)
    ll.curr = solution.merge_two_list_recursion(ll.curr, ll_2.curr)
    print(ll)
    
    
     
if __name__ == "__main__":
    main()
        