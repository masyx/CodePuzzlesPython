""" 104. Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
 

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""



import collections


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space
def find_maximum_depth(root):
    max_tree_depth = 0
    if root is None:
        return max_tree_depth
    queue = collections.deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        max_tree_depth += 1
        for _ in range(level_size):
            current_node = queue.popleft()
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return max_tree_depth

# O(n) time | O(log n) space for balanced binary tree, O(n) for unbalanced
def max_depth(root):
    if not root:
        return 0
    
    left_height = max_depth(root.left)
    right_height = max_depth(root.right)
    return max(left_height, right_height) + 1


def main():
    # Creating a simple binary tree manually
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)

    print(f"Max tree depth is: {find_maximum_depth(root)}")
    print(f"Max tree depth is: {max_depth(root)}")
    
    
    # Visual representation of the tree:
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    #   / \ /
    #  8  9 10


if __name__ == "__main__":
    main()