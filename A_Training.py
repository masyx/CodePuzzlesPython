class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h) space, where n is the number of the nodes
# and 'h' is the hight of the tree
class Solution:
    def mirror_binary_tree(self, root):
        def dfs_post_order(node):
            if not node:
                return
            
            dfs_post_order(node.left)
            dfs_post_order(node.right)
            
            node.left, node.right = node.right, node.left
        
        dfs_post_order(root)
        return root

def main():
    tree = BinaryTree(1)
    
    tree.left = BinaryTree(3)
    tree.right = BinaryTree(2)
    
    tree.left.left = BinaryTree(7)
    tree.left.right = BinaryTree(4)
    
    
    sol = Solution()
    sol.mirror_binary_tree(tree)
    
    
if __name__ == "__main__":
    main()