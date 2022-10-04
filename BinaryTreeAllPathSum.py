class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""The time complexity of the above algorithm is O(N^2), where N is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once (which will take O(N)), 
and for every leaf node, we might have to store its path 
(by making a copy of the current path) which will take O(N)."""
# O(n^2) time | O(n) space
def find_paths(root, sum):
    allPaths = []
    find_paths_helper(root, sum, [], allPaths)
    return allPaths

def find_paths_helper(current_node, sum, current_path, allPaths):
    if current_node is None:
        return
    current_path.append(current_node.val)
    if sum == current_node.val and current_node.left is None and current_node.right is None:
        allPaths.append(current_path[:])
    else:
        find_paths_helper(current_node.left, sum - current_node.val, current_path, allPaths)
        find_paths_helper(current_node.right, sum - current_node.val, current_path, allPaths)
    del current_path[-1]



def find_paths_2(root, sum):
    return find_paths_helper_2(root, sum, [], [])

def find_paths_helper_2(current_node, sum, current_path, allPaths):
    if current_node is None:
        return
    current_path.append(current_node.val)
    if sum == current_node.val and current_node.left is None and current_node.right is None:
        allPaths.append(current_path[:])
    else:
        find_paths_helper_2(current_node.left, sum - current_node.val, current_path, allPaths)
        find_paths_helper_2(current_node.right, sum - current_node.val, current_path, allPaths)
    del current_path[-1]
    return allPaths


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths_2(root, sum)))


if __name__ == "__main__":
    main()