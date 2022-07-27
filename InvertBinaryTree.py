class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    


def invertBinaryTree(tree):
    # Write your code here.
    pass





def initializeBinaryTree():
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)
    
    tree.left.left.left = BinaryTree(8)
    tree.left.left.right = BinaryTree(9)
    
    tree.right.left = BinaryTree(6)
    tree.right.right = BinaryTree(7)
    
    return tree


def main():
    tree = initializeBinaryTree()
    print(invertBinaryTree(tree))
    
if __name__ == "__main__":
    main()