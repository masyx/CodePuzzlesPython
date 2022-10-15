"""Given a binary tree and a number 'S', find all paths in the tree 
such that the sum of all the node values of each path equals 'S'. 
Please note that the paths can start or end at any node but all paths 
must follow direction from parent to child (top to bottom)."""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
# My solution: probably will be incorrect if tested intensively, just here for learning purpose
# O(n^2) time | O(d) space
def count_paths(root, S, result = []):
    if root is None:
        return
    has_path(root, S, [], result)
    count_paths(root.left, S, result)
    count_paths(root.right, S, result)
    return result

def has_path(node, sum, curr_path, result):
    if node is None:
      return
    curr_path.append(node.val)
    if node.val == sum and node.left is None and node.right is None:
      result.append(curr_path[:])
    return has_path(node.left, sum - node.val, curr_path, result) \
        or has_path(node.right, sum - node.val, curr_path, result)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))
    
    
if __name__ == "__main__":
    main()