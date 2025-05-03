import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def invertTreeRecursive(self, root):
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTreeRecursive(root.left)
        self.invertTreeRecursive(root.right)
        return root
    
    def invert_tree_iterative_dfs(self, root):
        if root is None:
            return None
        stack = [root]
        while stack:
            curr_node = stack.pop()
            curr_node.left, curr_node.right = curr_node.right, curr_node.left
            
            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)
        return root
    
    def invert_tree_iterative_bfs(self, root):
        if root is None:
            return None
        q = collections.deque([root])
        while q:
            curr = q.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root
                
                
        
        
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

    sol2 = Solution()
    # print(sol.dfs_inorder(root, []))
    # print(sol.dfs_inorder(root2, []))
    print(sol2.isSameTree(root, root2))
    
    
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
        