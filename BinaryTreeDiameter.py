''' 543. Diameter of Binary Tree
Easy

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''




'''Important notes

Depth of a Node: 
- The depth of a specific node is the number of edges from the root of the tree to that node.
- The root node has a depth of 0.
- Nodes directly connected to the root (its children) have a depth of 1, and so on.

Height of a Node:
- The height of a specific node is the number of edges on the longest path from that node to a leaf node in its subtree.
- A leaf node (a node with no children) has a height of 0.
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    # Key insight: diameter at node = height(left subtree) + height(right subtree)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  # global max
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursive depth calculation
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            
            # Update diameter at this node
            curr_diameter = left_h + right_h
            self.max_diameter = max(self.max_diameter, curr_diameter)
            
            # Return height of current node
            return 1 + max(left_h, right_h)
        
        dfs(root)
        return self.max_diameter



def main():
    '''
         1
        / \
       2   3
          / \
         4   5
        /     \
       6       7
      /         \
     8           9
    '''
    # Build the two deep chains in the right subtree:
    node8 = TreeNode(8)
    node6 = TreeNode(6, left=node8)
    node4 = TreeNode(4, left=node6)

    node9 = TreeNode(9)
    node7 = TreeNode(7, right=node9)
    node5 = TreeNode(5, right=node7)

    # Assemble the right subtree under node 3:
    node3 = TreeNode(3, left=node4, right=node5)

    # Simple left child of the root:
    node2 = TreeNode(2)

    # Finally, the root:
    root = TreeNode(1, left=node2, right=node3)

    sol = Solution()
    diameter = sol.diameterOfBinaryTree(root)
    print(diameter)
    
    
if __name__ == "__main__":
    main()