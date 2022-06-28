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
    
# O(n) time | O(h) space    
def nodeDepths(root):
    depths = []
    getNodesDepth(root, -1, depths)
    return sum(depths)
    
    
def getNodesDepth(node, currentDepth, depths):
    if node is None:
        return
    
    runningDepth = currentDepth + 1
    if runningDepth > 0:
        depths.append(runningDepth)
        print(f"The depth of the node with value {node.value} is: {runningDepth}")
    
    if node.left is None and node.right is None:
        return
    
    getNodesDepth(node.left, runningDepth, depths)
    getNodesDepth(node.right, runningDepth, depths)
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()