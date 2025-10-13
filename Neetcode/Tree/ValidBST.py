""" 98. Validate Binary Search Tree
Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys strictly less than the node's key.
- The right subtree of a node contains only nodes with keys strictly greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
      10
     /  \
   5     15
  / \
 3   12   ❌

Input: root = [10,5,15,3,12,null,null]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    #           3
    #       2        6
    #    0     5  4     9
    # 1 
    #
    #
    def isValidBST(self, root) -> bool:
        def valid(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            v = node.val
            if not low < v < high:
                return False
            return valid(node.left, low, v) and valid(node.right, v, high)
        return valid(root)


    def isValidBST(self, root) -> bool:
        def valid(node, lo=float('-inf'), hi=float('inf')):
            if not node:
                return True
            v = node.val
            if not lo < v < hi:
                return False

            # Short-circuit: only touch right if left is valid
            if not valid(node.left, lo, v):
                return False
            return valid(node.right, v, hi)
        return valid(root)



def main():
    
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(12)  # ❌ violates BST rule (should be < 10)

    sol = Solution()
    print(sol.isValidBST(root))
        
if __name__ == "__main__":
    main()