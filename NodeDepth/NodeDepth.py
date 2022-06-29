class BinaryTree:
    def __init__(self, root):
        self.value = root
        self.left = None
        self.right = None
        
        
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
    print(nodeDepths(tree))

    
# O(n) time | O(n) space    
def nodeDepths(root):
    depths = []
    getNodesDepth(root, depths)
    return sum(depths)
   
   
def getNodesDepth(node, depths, depth = 0):
    if node is None:
        return
    
    depths.append(depth)
    print(f"The depth of the node with value {node.value} is: {depth}")
    
    getNodesDepth(node.left, depths, depth + 1)
    getNodesDepth(node.right, depths, depth + 1)


    
if __name__ == "__main__":
    main()