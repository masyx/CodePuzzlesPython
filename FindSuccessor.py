class BinaryTree():
    def __init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(n) time | O(1) space
def find_successor(tree, node):
    result = []
    find_successor_helper(tree, node, result)
    if len(result) <= 1:
        return None
    else:
        return result[1]


def find_successor_helper(tree, node, result):
    if tree is not None:
        find_successor_helper(tree.left, node, result)
        if len(result) == 1:
            result.append(tree)
        if tree.value == node.value:
            result.append(node)
        find_successor_helper(tree.right, node, result)

# TODO write method with better time complexity, O(h) time
def find_successor(tree, node):
    return        
        
def main():
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)
    
    tree.left.left.left = BinaryTree(6)

    node = BinaryTree(3)

    found_node = find_successor(tree, node)
    if found_node:
        print(node.value)
    else:
        print('Nothing')
    
    
if __name__ == "__main__":
    main()