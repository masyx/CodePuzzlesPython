class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n^2) time | O(n) space where n is the length of the input array
def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None
    
    current_value = preOrderTraversalValues[0]
    right_subtree_idx = len(preOrderTraversalValues)
    for i in range(1, len(preOrderTraversalValues)):
        if preOrderTraversalValues[i] >= current_value:
            right_subtree_idx = i
            break

    left = reconstructBst(preOrderTraversalValues[1:right_subtree_idx])
    right = reconstructBst(preOrderTraversalValues[right_subtree_idx:])
    
    return BST(current_value, left, right)


def main():
    pre_order_traversal_values = [10, 4, 2, 5, 17, 19]
    tree = reconstructBst(pre_order_traversal_values)
    print(tree)
    
    
if __name__ == "__main__":
    main()