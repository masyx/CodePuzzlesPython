class BST():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validate_bst_helper(tree, float('-inf'), float('inf'))

# O(n) time | O(d) space
def validate_bst_helper(node, min, max):
    if node is None:
        return True
    if node.value < min or node.value >= max:
        return False
    left_is_valid = validate_bst_helper(node.left, min, node.value)
    # right_is_valid = validate_bst_helper(node.right, node.value, max)
    return left_is_valid and validate_bst_helper(node.right, node.value, max)

def main():
    tree = BST(3)
    tree.left = BST(1)
    tree.right = BST(5)

    tree.left.left = BST(-5)
    tree.left.right = BST(2)

    tree.left.left.left = BST(-10)
    tree.left.left.right = BST(99)
    print(validateBst(tree))
    
    
if __name__ == "__main__":
    main()