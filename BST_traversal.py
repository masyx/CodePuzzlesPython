class Node():
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


'''
         1
       /   \
      2     3
     /\     /\
    4  5   6  7
   /      / \
  8      9  10


Preorder traversal: [1, 2, 4, 8, 5, 3, 6, 9, 10, 7]
Inorder traversal: [8, 4, 2, 5, 1, 9, 6, 10, 3, 7]
Postorder traversal: [8, 4, 5, 2, 9, 10, 6, 7, 3, 1]
'''
def main():
    # tree = None
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.right.left.left = Node(9)
    root.right.left.right = Node(10)
    
    print(f"Preorder traversal recursive: {dfs_pre_order(root, [])}")
    print(f"Inorder traversal recursive: {dfs_in_order(root, [])}")
    print(f"Postorder traversal recursive: {dfs_post_order(root, [])}")
    print()
    print(f"Preorder traversal iterative: {dfs_pre_order_iterative(root)}")
    print(f"Inorder traversal iterative: {dfs_in_order_iterative(root)}")
    print(f"Postorder traversal iterative: {dfs_post_order_iterative(root)}")

if __name__ == '__main__':
    main()