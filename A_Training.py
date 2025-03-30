
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postOrderHelper(node, res):
            if not node:
                return

            if node.left:
                postOrderHelper(node.left, res)
            if node.right:
                postOrderHelper(node.right, res)
            if node.val:
                res.append(node.val)

        if not root:
            return []
        res = []
        if root.left:
            postOrderHelper(root.left, res)
        if root.right:
            postOrderHelper(root.right, res)
        
        res.append(root.val)
        return res

def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    sol = Solution()
    print(sol.postorderTraversal(root))
    
     
if __name__ == "__main__":
    main()
        