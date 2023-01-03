import collections
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h) space, where n is the number of the nodes
# and 'h' is the hight of the tree
def mirror_binary_tree_recursive(node):
    if not node:
        return
    
    node.left, node.right = node.right, node.left
    
    mirror_binary_tree_recursive(node.left)
    mirror_binary_tree_recursive(node.right)
    
    return node

def mirror_binary_tree_iterative(node):
    if not node:
        return
    
    queue = collections.deque([node])

    while queue:
        current_node = queue.pop()

        current_node.left, current_node.right = \
            current_node.right, current_node.left
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
            
    return node

def main():
    tree = BinaryTree(1)
    
    tree.left = BinaryTree(3)
    tree.right = BinaryTree(2)
    
    tree.left.left = BinaryTree(7)
    tree.left.right = BinaryTree(4)
    
    
    #tree_1 = mirror_binary_tree_recursive(tree)
    tree_2 = mirror_binary_tree_iterative(tree)
    print()
    
    
if __name__ == "__main__":
    main()