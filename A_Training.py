import collections
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)] # a pair (node, depth)
        max_depth = 0
        while stack:
            curr_node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if curr_node.left:
                stack.append((curr_node.left, depth + 1))
            if curr_node.right:
                stack.append((curr_node.left, depth + 1))
        return max_depth
            
                
        
        
def main():
    # Creating a simple binary tree manually
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    # root.left.left.left = TreeNode(8)
    # root.left.left.right = TreeNode(9)
    # root.left.right.left = TreeNode(10)
    
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)

    sol = Solution()
    # print(sol.dfs_inorder(root, []))
    # print(sol.dfs_inorder(root2, []))
    print(sol.maxDepth(root))
    
    
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
        