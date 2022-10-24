import collections


class BinaryTree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def branchSums(root):
    result = []
    branch_sums_recursive(root, 0, result)
    return result

def branch_sums_recursive(node, current_sum, array):
    if node is None:
        return
    current_sum += node.value
    if not node.left and not node.right:
        array.append(current_sum)
    branch_sums_recursive(node.left, current_sum, array)
    branch_sums_recursive(node.right, current_sum, array)


def initializeBinaryTree():
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)
    
    tree.left.left.left = BinaryTree(8)
    tree.left.left.right = BinaryTree(9)
    
    tree.right.left = BinaryTree(6)
    tree.right.right = BinaryTree(7)
    
    return tree


def main():
    tree = initializeBinaryTree()
    print(branchSums(tree))


main()