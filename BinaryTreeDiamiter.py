class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

def binaryTreeDiameter(tree):
    return - 1


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
    
    
    print(binaryTreeDiameter(tree))
    
    
if __name__ == "__main__":
    main()