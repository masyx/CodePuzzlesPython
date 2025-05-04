"""572. Subtree of Another Tree
Easy

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same 
structure and node values of subRoot and false otherwise.A subtree of a binary tree tree is a tree that consists 
of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 
Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

subRoot is a subtree of root
 Tree structure:
        3
       / \
      4   5
     / \
    1   2
 subRoot:
      4
     / \
    1   2

subRoot is NOT a subtree of root   
 Tree structure:
        3
       / \
      4   5
     / \
    1   2
         \
          0
 subRoot:
      4
     / \
    1   2
"""


from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    #O(m*n) time | O(m + n) space
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or \
            self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.isSameTree(root1.left, root2.left) and \
            self.isSameTree(root1.right, root2.right)
            
            
def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    # root.left.left.left = TreeNode(8)
    # root.left.left.right = TreeNode(9)
    # root.left.right.left = TreeNode(10)
    
    root2 = TreeNode(2)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    # root2.left.left = TreeNode(8)
    
    sol = Solution()
    
    print(f"Is root2 is a subtree of root? {'yes' if sol.isSubtree(root, root2) else 'No'}")
    
    # Visual representation of the tree:
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    #   / \ /
    #  8  9 10

if __name__ == "__main__":
    main()