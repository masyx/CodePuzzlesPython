class BST():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# FOR ALL 3 FUNCTIONS: O(n) time | O(n) space, but if we didn't have to return an array
# space complexity would be O(d), where d is the depth of the tree
def dfs_in_order(root, visited):
    if root:
        visited.append(root.value)
        dfs_in_order(root.left, visited)
        dfs_in_order(root.right, visited)
    return visited


def dfs_pre_order(root, visited: list): 
    if root:
        visited.append(root.value)
        dfs_pre_order(root.left, visited)
        dfs_pre_order(root.right, visited)
    return visited

def dfs_pre_order_iterative(root, visited: list):
    stack = [root]
    while stack:
        current_node = stack.pop()
        if current_node is None:
            continue
        visited.append(current_node.value)
        stack.append(current_node.right)
        stack.append(current_node.left)
    return visited

def dfs_post_order(tree, array):
    if tree is not None:
        dfs_post_order(tree.left, array)
        dfs_post_order(tree.right, array)
        array.append(tree.value)
    return array


def main():
    tree = BST(0)
    
    tree.left = BST(1)
    tree.right = BST(2)
    
    tree.left.left = BST(3)
    tree.left.right = BST(4)
    
    tree.right.left = BST(5)
    tree.right.right = BST(6)

    print(f"In-order traversal recursive: {dfs_pre_order(tree, [])}")
    
    # print(f"Pre-order traversal recursive: {dfs_pre_order(tree, [])}")
    # print(f"Pre-order traversal iterative: {dfs_pre_order_iterative(tree, [])}")
    # result.clear()
    
    # print(f"Post-order traversal recursive: {dfs_pre_order(tree, [])}")
    # print(dfs_post_order(tree, result))


if __name__ == '__main__':
    main()
