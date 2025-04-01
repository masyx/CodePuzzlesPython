
from typing import List, Optional


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
        count += self.generate_bin(n, f"{current}0")
        count += self.generate_bin(n, f"{current}1")
        return count
        
def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    sol = Solution()
    print(sol.post_order_traversal(root))
    
    print("Generate possible binary numbers: ")
    sol.generate_bin(12)
    
     
if __name__ == "__main__":
    main()
        