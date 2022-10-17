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

def count_paths_recursive(current_node, S, current_path):
    if current_node is None:
        return 0
    current_path.append(current_node.val)
    path_count, path_sum = 0, 0
    # find the sum of all sub-paths in the current path list
    for i in range(len(current_path) - 1, -1, -1):
        path_sum += current_path[i]
        if path_sum == S:
            path_count += 1
    path_count += count_paths_recursive(current_node.left, S, current_path)
    path_count += count_paths_recursive(current_node.right, S, current_path)
    
    del current_path[-1]
    return path_count


def main():
    root = TreeNode(12)
    root.left = TreeNode(6)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.left.left = TreeNode(0)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 18)))
    
    
if __name__ == "__main__":
    main()