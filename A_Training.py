
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def post_order_traversal_helper(self, node, res):
            if not node:
                return
            self.post_order_traversal_helper(node.left, res)
            self.post_order_traversal_helper(node.right, res)
            res.append(node.val)
    
    def post_order_traversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.post_order_traversal_helper(root, res)        
        return res
    
    def generate_bin(self, n, current = "") -> int:
        if len(current) == n:
            print(current)
            return 1
        
        count = 0
        count += self.generate_bin(n, current + "0")
        count += self.generate_bin(n, current + "1")
        return count
    
    def generate_parentheses_bf(self, n):
        def is_valid(s):
            count = 0
            for c in s:
                count += 1 if c == "(" else -1
                if count < 0:
                    return False
            return count == 0
        
        res = []
        queue = deque([""])
        while queue:
            curr = queue.popleft()
            if len(curr) == 2 * n:
                if is_valid(curr):
                    res.append(curr)
                continue
            
            queue.append(curr + "(")
            queue.append(curr + ")")
            
        return res
            
            
        
    
    
    
def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    sol = Solution()
    print(sol.post_order_traversal(root))
    
    print("Generate possible binary numbers: ")
    print(f"The total number of possible binary combinations is: {sol.generate_bin(4)}")
    
    print(sol.generate_parentheses_bf(5))
    
     
if __name__ == "__main__":
    main()
        