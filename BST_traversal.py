class BST():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# FOR ALL 3 FUNCTIONS: O(n) time | O(n) space, but if we didn't have to return an array
# space complexity would be O(d), where d is the depth of the tree

# Pre-Order Traversals
def dfs_pre_order(node, visited: list):
    if node:
        visited.append(node.value)
        dfs_pre_order(node.left, visited)
        dfs_pre_order(node.right, visited)
    return visited

def dfs_pre_order_iterative(node):
    visited = []
    stack = [node]
    while stack:
        current_node = stack.pop()
        if current_node:
            visited.append(current_node.value)
            stack.append(current_node.right) # add right child first
            stack.append(current_node.left)
    return visited


# In-Order Traversals
def dfs_in_order(node, visited: list):
    if node:
        dfs_in_order(node.left, visited)
        visited.append(node.value)
        dfs_in_order(node.right, visited)
    return visited

def dfs_in_order_iterative(node):
    visited = []
    stack = []
    current_node = node
    while stack or current_node:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        visited.append(current_node.value)
        current_node = current_node.right
    return visited


# Post-Order Traversal
def dfs_post_order(node, visited: list):
    if node:
        dfs_post_order(node.left, visited)
        dfs_post_order(node.right, visited)
        visited.append(node.value)
    return visited

def dfs_post_order_iterative(node):
    visited = []
    stack = [node]
    while stack:
        current_node = stack.pop()
        if current_node:
            visited.append(current_node.value)
            stack.append(current_node.left)
            stack.append(current_node.right)
    return visited[::-1]


def main():
    # tree = None
    tree = BST(0)
    
    tree.left = BST(1)
    tree.right = BST(2)
    
    tree.left.left = BST(3)
    tree.left.right = BST(4)
    
    tree.right.left = BST(5)
    tree.right.right = BST(6)

    print(f"Pre-order traversal recursive: {dfs_pre_order(tree, [])}")
    print(f"Pre-order traversal iterative: {dfs_pre_order_iterative(tree)}\n")

    print(f"In-order traversal recursive: {dfs_in_order(tree, [])}")
    print(f"In-order traversal iterative: {dfs_in_order_iterative(tree)}\n")
    
    print(f"Post-order traversal recursive: {dfs_post_order(tree, [])}")
    print(f"Post-order traversal iterative: {dfs_post_order_iterative(tree)}")


if __name__ == '__main__':
    main()