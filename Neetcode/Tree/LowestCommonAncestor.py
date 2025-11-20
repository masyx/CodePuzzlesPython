class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #      5
    #    2   6
    #     4
    #p: 4, q: 6; res = 5
    #
    #
    #
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        
        # Case 1: Both p and q are smaller than the current root.
        # The LCA must be in the left subtree.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # Case 2: Both p and q are larger than the current root.
        # The LCA must be in the right subtree.
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # Case 3: We found the split.
        # Either one is on the left and one on the right, OR
        # the current root is actually p or q itself.
        else:
            return root
    
    
    
    

if __name__ == "__main__":
    # ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    root = TreeNode(5, TreeNode(2, None, TreeNode(4)), TreeNode(6))
    sol = Solution()
    print(sol.lowestCommonAncestor(root, TreeNode(1), TreeNode(0)).val)
    
    
