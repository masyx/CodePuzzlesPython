import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def max_depth_dfs_rec(self, root):
        if root is None:
            return 0
        
        left = self.max_depth_dfs_rec(root.left)
        right = self.max_depth_dfs_rec(root.right)
        
        return 1 + max(left, right)
    
    def max_depth_dfs_iter(self, root):
        if root is None:
            return 0
        stack = [(root, 1)]
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
            
            max_depth = max(max_depth, depth)
        
        return max_depth 
            
    
    def max_depth_bfs_iter(self, root):
        q = collections.deque()
        if root:
            q.append(root)
        level = 0
        
        while q:
            level += 1
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return level
             
def main():
    # Visual representation of the tree:
    #         1
    #       /   \
    #      2     3
    #     / \   /
    #    4   5 6
    #     \ 
    #      9
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.left.left.right = TreeNode(9)
    
    sol = Solution()

    print(f"Max tree depth is: {sol.max_depth_dfs_rec(root)}")
    print(f"Max tree depth is: {sol.max_depth_dfs_iter(root)}")
    print(f"Max tree depth is: {sol.max_depth_bfs_iter(root)}")



if __name__ == "__main__":
    main()
        