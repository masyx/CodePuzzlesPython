import collections
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSameTreeRecursion(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTreeRecursion(p.left, q.left)  \
            and self.isSameTreeRecursion(p.right, q.right)
    
    def isSameTreeIterative(self, p, q):
        q = deque()
        q.append((q, p))
        while q:
            node_1, node_2 = q.popleft()
            if not node_1 and not node_2:
                continue
            if not node_1 or not node_2:
                return False
            if node_1.val != node_2.val:
                return False
            
            q.append((p.left, q.left))
            q.append((p.right, q.right))
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
    root2.left.left = TreeNode(44)

    sol = Solution()
    # print(sol.dfs_inorder(root, []))
    # print(sol.dfs_inorder(root2, []))
    print(sol.isSameTreeRecursion(root, root2))
    print(sol.isSameTreeIterative(root, root2))
    
    
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
        