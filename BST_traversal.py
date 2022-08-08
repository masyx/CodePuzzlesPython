class BST():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inOrderTraverse(tree, array):



def preOrderTraverse(tree, array):
    # Write your code here.
    pass


def postOrderTraverse(tree, array):
    # Write your code here.
    pass


def main():
    tree = BST(3)
    tree.left = BST(1)
    tree.right = BST(5)
    
    tree.left.left = BST(-5)
    tree.left.right = BST(2)
    
    tree.left.left.left = BST(-10)
    
    result_in_order = []
    inOrderTraverse(tree, result_in_order)
    print(result_in_order)

if __name__ == '__main__':
    main()