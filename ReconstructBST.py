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


class TreeInfo:
    def __init__(self, root_idx):
        self.root_idx = root_idx


# O(n) time | O(n) space, where n is the length of the array
def reconstructBst_2(preOrderTraversalValues):
    tree_info = TreeInfo(0)
    return reconstruct_bst_from_range(float("-inf"), float("inf"), preOrderTraversalValues, tree_info)


def reconstruct_bst_from_range(lower_bound, upper_bound, 
                               pre_order_traversal_values, current_subtree_info: TreeInfo):
    if current_subtree_info.root_idx == len(pre_order_traversal_values):
        return None
    
    root_value = pre_order_traversal_values[current_subtree_info.root_idx]
    if root_value < lower_bound or root_value >= upper_bound:
        return None
    
    current_subtree_info.root_idx += 1
    left = reconstruct_bst_from_range(lower_bound, root_value, pre_order_traversal_values, current_subtree_info)
    right = reconstruct_bst_from_range(root_value, upper_bound, pre_order_traversal_values, current_subtree_info)
    return BST(root_value, left, right)


def main():
    pre_order_traversal_values = [10, 4, 2, 5, 17, 19]
    tree = reconstructBst_2(pre_order_traversal_values)
    print(tree)
    
    
if __name__ == "__main__":
    main()