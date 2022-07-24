class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
                
        
def nodeDepths(root, depth = 0):
    if root is None:
        return 0
    l = nodeDepths(root.left, depth + 1)
    r = nodeDepths(root.right, depth + 1)
    sum = depth + l + r
    return sum




def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    # root.left.left = BinaryTree(4)
    # root.left.right = BinaryTree(5)
    # root.right = BinaryTree(3)
    print(nodeDepths(root))
    print()
    
if __name__ == "__main__":
    main()