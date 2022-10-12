'''Given a binary tree and a number sequence, find if the sequence is present as 
a root-to-leaf path in the given tree.'''

import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def DFS_pre_order_traversal(root, bfs):
    if root is None:
        return
    bfs.append(root.val)
    DFS_pre_order_traversal(root.left, bfs)
    DFS_pre_order_traversal(root.right, bfs)
    
def pre_order_traversal_iterative(root):
    result = []
    if root is None:
        return result
    stack = [root]
    while stack:
        current = stack.pop()
        if current is None:
            continue
        result.append(current.val)
        stack.append(current.right)
        stack.append(current.left)
    return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    bfs = []
    DFS_pre_order_traversal(root, bfs)
    print(bfs)
    print(pre_order_traversal_iterative(root))

main()