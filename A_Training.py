class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
                
# O(n) time | O(d) space     
def nodeDepths(root, depth = 0):
    if root is None:
        return 0
    l = nodeDepths(root.left, depth + 1)
    r = nodeDepths(root.right, depth + 1)
    sum = depth + l + r
    return sum


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




def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    # root.left.left = BinaryTree(4)
    # root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    print(nodeDepthIterative(root))
    print()
    
if __name__ == "__main__":
    main()