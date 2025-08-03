"""100. Same Tree
Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""


from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree_extra_space(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs_inorder(p, []) == self.dfs_inorder(q, [])

    def dfs_inorder(self, root: TreeNode, result: List[int])-> List[int]:
        if not root:
            result.append(None)
            return
        
        result.append(root.val)
        self.dfs_inorder(root.left, result)
        self.dfs_inorder(root.right, result)
        return result
    
    def is_same_tree_recursion(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            return p is q
        
        return (p.val == q.val
                and self.is_same_tree_recursion(p.left, q.left)
                and self.is_same_tree_recursion(p.right, q.right))
    
    def is_same_tree_iterative(self, p, q):
        stack = [(p, q)]
        
        while stack:
            p, q = stack.pop()
            
            if p is None or q is None:
                if p is not q:
                    return False
                continue
        
            if p.val != q.val:
                return False
            
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
        return True
              
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
    root2.left.right = TreeNode(4)

    sol2 = Solution()
    # print(sol.dfs_inorder(root, []))
    # print(sol.dfs_inorder(root2, []))
    print(sol2.is_same_tree_recursion(root, root2))
    print(sol2.is_same_tree_iterative(root, root2))
    
    
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
        