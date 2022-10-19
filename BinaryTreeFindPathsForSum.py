"""Given a binary tree and a number 'S', find all paths in the tree 
such that the sum of all the node values of each path equals 'S'. 
Please note that the paths can start or end at any node but all paths 
must follow direction from parent to child (top to bottom)."""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

"""The time complexity of the above algorithm is O(N^2) in the worst case, where 'N' is the 
total number of nodes in the tree. This is due to the fact that we traverse each node once, 
but for every node, we iterate the current path. The current path, in the worst case, can be O(N)
(in the case of a skewed tree). But, if the tree is balanced, then the current path will be 
equal to the height of the tree, i.e., O(logN). So the best case of our algorithm will be O(N*logN)."""
# O(n^2) time worse, O(n*log(n)) average| O(n) space
def count_paths_2(root, S):
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

# O(n) time | O(n) space
def count_paths(root, target_sum):
    # hash table to store prefix sum
    map = {}
    return count_paths_prefix_sum(root, target_sum, map, 0)

def count_paths_prefix_sum(current_node, target_sum, prefixSums_map, current_path_sum):
    if current_node is None:
        return 0
    path_count = 0
    current_path_sum += current_node.val
    if current_path_sum == target_sum:
        path_count += 1
    prefixSums_map[current_path_sum] = prefixSums_map.get(current_path_sum, 0) + 1
    path_count += prefixSums_map.get(current_path_sum - target_sum, 0)
    
    path_count += count_paths_prefix_sum(current_node.left, target_sum, prefixSums_map, current_path_sum)
    path_count += count_paths_prefix_sum(current_node.right, target_sum, prefixSums_map, current_path_sum)
    
    prefixSums_map[current_path_sum] = prefixSums_map[current_path_sum] - 1
    return path_count

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