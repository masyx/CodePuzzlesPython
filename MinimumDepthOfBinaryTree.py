from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# O(n) time | O(n) space
def find_minimum_depth(root):
    min_tree_depth = 0
    if root is None:
        return min_tree_depth
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        min_tree_depth += 1
        for _ in range(level_size):
            current_node = queue.popleft()
            
            if not current_node.left and not current_node.right:
                return min_tree_depth
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    #print("Tree Minimum Depth: " + str(find_minimum_depth_recursive(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth_recursive(root)))


main()