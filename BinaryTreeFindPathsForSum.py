"""Given a binary tree and a number 'S', find all paths in the tree 
such that the sum of all the node values of each path equals 'S'. 
Please note that the paths can start or end at any node but all paths 
must follow direction from parent to child (top to bottom)."""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# O(n^2) time | O(n) space
def count_paths(root, S):
    return count_paths_recursive(root, S, [])
    
def count_paths_recursive(node, S, current_path):
    if node is None:
        return 0
    current_path.append(node.val)
    path_sum = paths_count = 0
    for i in range(len(current_path) - 1, -1, -1):
        path_sum += current_path[i]
        if path_sum == S:
            paths_count += 1
    paths_count += count_paths_recursive(node.left, S, current_path)
    paths_count += count_paths_recursive(node.right, S, current_path)
    
    del current_path[-1]
    return paths_count


def main():
    root = TreeNode(12)
    root.left = TreeNode(6)
    root.right = TreeNode(1)
    root.left.left = TreeNode(12)
    #root.left.left.left = TreeNode(0)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 18)))
    
    
if __name__ == "__main__":
    main()