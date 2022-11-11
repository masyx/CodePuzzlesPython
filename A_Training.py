class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findClosestValueInBst(tree, target):
    return 

def main():
    tree = BST(10)
    tree.left = BST(5)
    tree.right = BST(13)
    
    # tree.left.left = BST(2)
    # tree.left.right = BST(5)
    
    # tree.left.left.left = BST(1)
    
    # tree.right.left = BST(13)
    # tree.right.right = BST(22)
    
    # tree.right.left.right = BST(14)
    print(findClosestValueInBst(tree, 12))
    
    
if __name__ == "__main__":
    main()