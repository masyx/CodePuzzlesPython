class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h) space, where n is the number of the nodes
# and 'h' is the hight of the tree
class Solution:
    def diameter_of_binaryTree(self, node: BinaryTree) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        
        dfs(node)
        return self.diameter
        
def main():
    tree = BinaryTree(1)
    
    tree.left = BinaryTree(3)
    tree.right = BinaryTree(2)
    
    tree.left.left = BinaryTree(7)
    tree.left.right = BinaryTree(4)
    
    tree.left.left.left = BinaryTree(8)
    tree.left.left.left.left = BinaryTree(9)
    
    tree.left.right.right = BinaryTree(5)
    tree.left.right.right.right = BinaryTree(6)
    
    sol = Solution()
    diameter = sol.diameter_of_binaryTree(tree)
    print(diameter)
    
    
if __name__ == "__main__":
    main()