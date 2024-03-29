class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
# O(n) time | O(h) space, where 'n' is the number of nodes in the tree
# and 'h' is the height of the tree
def binaryTreeDiameter(tree):
    global longest_path
    longest_path = 0
    calculate_longest_path(tree)
    return longest_path


def calculate_longest_path(node):
    global longest_path
    if node is None:
        return 0
    left_depth = calculate_longest_path(node.left)
    right_depth = calculate_longest_path(node.right)
    
    current_longest_path = left_depth + right_depth
    longest_path = max(current_longest_path, longest_path)
    return max(left_depth, right_depth) + 1

# O(n) time | O(h) space, where 'n' is the number of nodes in the tree
# and 'h' is the height of the tree
class Solution():
    def diameter_of_binaryTree(self, root: BinaryTree) -> int:
        """
        :type root: BinaryTree
        :retype: int
        """
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_branch_hight = dfs(node.left)
            right_branch_hight = dfs(node.right)
            
            self.diameter = max(self.diameter, left_branch_hight + right_branch_hight)
            return 1 + max(left_branch_hight, right_branch_hight)
        
        dfs(root)
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