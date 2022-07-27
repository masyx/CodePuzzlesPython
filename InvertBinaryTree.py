class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    


def invertBinaryTreeMy(tree: BinaryTree):
    if tree.left is not None:
        invertBinaryTreeMy(tree.left)
    if tree.right is not None:
        invertBinaryTreeMy(tree.right)
    
    if tree.left is not None or tree.right is not None:
        tree.left, tree.right = tree.right, tree.left
    else:
        return 
    
    
def invertBinaryTree(tree):
    if tree is None:
        return 
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    
def invertBinaryTreeQueue(tree):
    queue = [tree]
    while len(queue):
        currentNode = queue.pop(0)
        if currentNode is None:
            continue
        currentNode.left, currentNode.right = currentNode.right, currentNode.left
        queue.append(currentNode.left)
        queue.append(currentNode.right)





def initializeBinaryTree():
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    # tree.right = BinaryTree(3)
    
    # tree.left.left = BinaryTree(4)
    # tree.left.right = BinaryTree(5)
    
    # tree.left.left.left = BinaryTree(8)
    # tree.left.left.right = BinaryTree(9)
    
    # tree.right.left = BinaryTree(6)
    # tree.right.right = BinaryTree(7)
    
    return tree


def main():
    tree = initializeBinaryTree()
    print(invertBinaryTreeQueue(tree))
    print
    
if __name__ == "__main__":
    main()