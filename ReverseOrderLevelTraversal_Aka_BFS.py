from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse(root):
    result = deque()
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        result.appendleft(current.val)
        if current.right:
            queue.append(current.right)
        if current.left:
            queue.append(current.left)
    return result

# O(n) time 
# O(n) space  as we need to return a list containing the level order traversal. We will also need O(N) space for the queue. 
# Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), 
# therefore we will need O(N) space to store them in the queue.
def traverse_2(root):
    result = deque()
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft(queue)
            current_level.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.appendleft(current_level)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
