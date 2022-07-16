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
    print(nodeDepthIterative(tree))

    
# O(n) time | O(n) space    
def nodeDepthsMy(root):
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

# O(n) time | O(h) space, tha maximum number of function calls on a call stack at one point
# is going to be the hight of the binary tree(or the depth of the deepest node in the binary tree) and
# if the binary tree is balanced the O(h) space becomes really close to O(log(n)) because we are eliminating half of the tree
# with every step
def nodeDepths(root, depth = 0):
    if root is None:
        return 0
    left = nodeDepths(root.left, depth + 1)
    right = nodeDepths(root.right, depth + 1)
    return depth + left + right


def nodeDepthIterative(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth +1})
    return sumOfDepths
  

    
if __name__ == "__main__":
    main()