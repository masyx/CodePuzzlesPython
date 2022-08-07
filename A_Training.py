class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    arr = []
    branch_sums_helper(root, arr, 0)
    return arr


def branch_sums_helper(node, sums, running_sum):
    if node is None:
        return
    running_sum += node.value
    if node.left is None and node.right is None:
        sums.append(running_sum)
    branch_sums_helper(node.left, sums, running_sum)
    branch_sums_helper(node.right, sums, running_sum)

def main():
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    
    tree.left.left = BinaryTree(4)
    # tree.left.right = BinaryTree(5)
    
    # tree.left.left.left = BinaryTree(8)
    # tree.left.left.right = BinaryTree(9)
    
    # tree.right.left = BinaryTree(6)
    # tree.right.right = BinaryTree(7)

    print(branch_sums(tree))
    
if __name__ == "__main__":
    main()