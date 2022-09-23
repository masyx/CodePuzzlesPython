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


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_maximum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_maximum_depth(root)))


if __name__ == "__main__":
    main()