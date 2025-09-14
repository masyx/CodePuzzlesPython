"""110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    # O(n) time | O(h) space where h is the height of the tree
    # Space best case: O(log n) - balanced tree
    # Space worst case: O(n) - degenerate tree (tree becomes linked list)
    def isBalancedBottomUp(self, root):
        def isBalancedHelper(root):
            if root is None:
                return 0
            
            left_height = isBalancedHelper(root.left)
            if left_height == -1:
                return -1
            
            right_height = isBalancedHelper(root.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return isBalancedHelper(root) != -1
    
#               1
#           2       3
#       5
#   7
#    
def main():
  root = TreeNode(1, TreeNode(2, TreeNode(5, TreeNode(7))), TreeNode(3))
  #root = None
  sol = Solution()
  print(sol.isBalancedBottomUp(root))
  
  
if __name__ == "__main__":
    main()