from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# O(n) time | O(n) space
def find_successor_my(root, key):
    if root is None:
        return None
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        if current.val == key:
            break
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return queue[0] if queue else None


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    result = find_successor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    
    result = find_successor(root, 9)
    if result:
        print(result.val)
    
    result = find_successor(root, 12)
    if result:
        print(result.val)


main()