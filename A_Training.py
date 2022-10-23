class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def nodeDepths_recursive(root, depth = 0):
    if root is None:
        return 0
    l = nodeDepths(root.left, depth + 1)
    r = nodeDepths(root.right, depth + 1)
    return depth + l + r


def nodeDepths(root):
    stack = [{"node": root, "depth": 0}]
    depths_sum = 0
    while stack:
        current_node_info = stack.pop()
        curr_node, curr_depth = current_node_info["node"], current_node_info["depth"]
        if curr_node is None:
            continue
        depths_sum += curr_depth
        stack.append({"node": curr_node.left, "depth": curr_depth + 1})
        stack.append({"node": curr_node.right, "depth": curr_depth + 1})
    return depths_sum

def initializeBinaryTree():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    
    tree.left.left.left = TreeNode(8)
    tree.left.left.right = TreeNode(9)
    
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    
    return tree


def main():
    tree = initializeBinaryTree()
    print(nodeDepths(tree))


main()