class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

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


class Solution():
    def diameterOfBinaryTree(self, root):
        """
        :type root: BinaryTree
        :rtype: int
        """
        self.max =0
        
        def levels(root):
            if not root: 
                return 0
            left = levels(root.left)
            right = levels(root.right)
            self.max = max(self.max, left + right)
            return 1 + max(left, right)
        
        levels(root)
        return self.max


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
    diameter = sol.diameterOfBinaryTree(tree)
    print(diameter)
    
    
if __name__ == "__main__":
    main()