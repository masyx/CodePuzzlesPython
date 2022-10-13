'''Given a binary tree and a number sequence, find if the sequence is present as 
a root-to-leaf path in the given tree.'''

import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root, sequence):
    result = []
    find_path_recursive(root, sequence, result)
    if result:
        return True
    else:
        return False

def find_path_recursive(root, sequence, result, current = []):
    if root is not None:
        current.append(root.val)
        find_path_recursive(root.left, sequence, result)
        find_path_recursive(root.right, sequence, result)
        if current == sequence:
            result.append(f"Found sequence: {sequence}")
        del current[-1]


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Tree has path sequence: " + str(find_path(root, [1, 0, 1])))
    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()