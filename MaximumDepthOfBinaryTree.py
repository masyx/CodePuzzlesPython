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

# O(n) time | O(log n) space for balanced binary tree, O(n) for unbalanced
def max_depth_dfs_recursion(root):
    if not root:
        return 0
    
    left_height = max_depth(root.left)
    right_height = max_depth(root.right)
    return max(left_height, right_height) + 1

def max_depth_dfs_iterative(root):
    if not root:
        return 0
    stack = [(root, 1)] # stack holds a pair (node, depth)
    max_depth = 0
   
    while stack:
        curr, depth = stack.pop()
        max_depth = max(max_depth, depth)
        if curr.left:
            stack.append((curr.left, depth + 1))
        if curr.right:
            stack.append((curr.right, depth + 1))
    
    return max_depth

# O(n) time | O()
def max_depth_bfs(root):
    queue = collections.deque()
    if root:
        queue.append(root)
    level = 0
    
    while queue:
        level += 1
        for i in range(len(queue)):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
    return level


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

    print(f"Max tree depth is: {max_depth_bfs(root)}")
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