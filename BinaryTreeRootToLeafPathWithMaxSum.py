class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxRootToLeafPathSum(root):
    allPaths = []
    find_paths_helper(root, [], allPaths)
    return max(allPaths)

def find_paths_helper(current_node, current_path, allPaths):
    if current_node is None:
        return 
    current_path.append(current_node.val)
    if current_node.left is None and current_node.right is None:
        allPaths.append(sum(current_path[:]))
    find_paths_helper(current_node.left, current_path, allPaths)
    find_paths_helper(current_node.right, current_path, allPaths)
    del current_path[-1]



#O(n) time | O(n) space
def maxRootToLeafPathSum_2(root):
    allPaths = []
    find_paths_helper_2(root, 0, allPaths)
    return max(allPaths)

def find_paths_helper_2(current_node, current_path_sum, allPaths):
    if current_node is None:
        return 
    current_path_sum += current_node.val
    if current_node.left is None and current_node.right is None:
        allPaths.append(current_path_sum)
    find_paths_helper_2(current_node.left, current_path_sum, allPaths)
    find_paths_helper_2(current_node.right, current_path_sum, allPaths)
    current_path_sum -= current_node.val

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(11)
    root.right.right = TreeNode(5)
    print(maxRootToLeafPathSum(root))
    print(maxRootToLeafPathSum_2(root))

if __name__ == "__main__":
    main()