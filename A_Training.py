class TreeNode:
    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

'''
Original:
    1
   / \
  2   3
 / \ / \
4  5 6  7

Inverted:
    1
   / \
  3   2
 / \ / \
7  6 5  4

'''

def invert_binary_tree(root):
    if not root:
        return
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    root.left, root.right = root.right, root.left
    return root


def print_in_order(node):
    if not node:
        return
    print_in_order(node.left)
    print(node.value, end=' ')
    print_in_order(node.right)
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print("Original: ")
    print_in_order(root)
    
    print("\nInverted: ", )
    print_in_order(invert_binary_tree(root))
