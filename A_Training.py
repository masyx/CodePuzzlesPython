from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#               1
#           2       3
#       5
#   7
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # O(n) time | O(h) space where h is the height of the tree
    # Space best case: O(log n) - balanced tree
    # Space worst case: O(n) - degenerate tree (tree becomes linked list)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root) != -1

    def isBalancedHelper(self, root: Optional[TreeNode]):
        if not root:
            return 0
        
        left_height = self.isBalancedHelper(root.left)
        if left_height == -1:
            return -1
        
        right_height = self.isBalancedHelper(root.right)
        if right_height == -1:
            return -1
            
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
        
        
    
    
    
    
    
def main():
  root = TreeNode(1, TreeNode(2, TreeNode(5, TreeNode(7))), TreeNode(3))
  #root = None
  sol = Solution()
  print(sol.isBalanced(root))
  
  
if __name__ == "__main__":
    main()