class BST():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# FOR ALL 3 FUNCTIONS: O(n) time | O(n) space, but if we didn't have to return an array
# space complexity would be O(d), where d is the depth of the tree
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

def DFS_pre_order(root, visited: list): 
    if root:
        visited.append(root.value)
        DFS_pre_order(root.left, visited)
        DFS_pre_order(root.right, visited)
    return visited

def DFS_pre_order_iterative(root, visited: list):
    stack = [root]
    while stack:
        current_node = stack.pop()
        if current_node is None:
            continue
        visited.append(current_node.value)
        stack.append(current_node.right)
        stack.append(current_node.left)
    return visited

def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


def main():
    tree = BST(3)
    tree.left = BST(1)
    tree.right = BST(5)
    tree.left.left = BST(-5)
    tree.left.right = BST(2)
    tree.left.left.left = BST(-10)

    result = []
    print(inOrderTraverse(tree, result))
    result.clear()
    
    print(f"Pre-order traversal recursive: {preOrderTraverse(tree, result)}")
    print(f"Pre-order traversal recursive: {DFS_pre_order(tree, [])}")
    print(f"Pre-order traversal iterative: {DFS_pre_order_iterative(tree, [])}")
    result.clear()
    
    print(postOrderTraverse(tree, result))


if __name__ == '__main__':
    main()
