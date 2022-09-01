class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    return None


def main():
    pre_order_traversal_values = [10, 4, 2, 5, 17, 19]
    tree = reconstructBst(pre_order_traversal_values)
    print(tree)