from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  # global max
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursive depth calculation
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Update diameter at this node
            self.max_diameter = max(self.max_diameter, left + right)
            
            # Return height of current node
            return 1 + max(left, right)
        
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