from collections import deque


class TreeNode:
    def __init__(self, val):
      self.val = val
      self.left, self.right = None, None

# O(n) time, where n is the number of nodes in the tree
# O(n) space, we need to return a list containing level order traversal. We will also have to store nodes in the queue
def traverse(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
      current = queue.popleft()
      result.append(current.val)
      if current.left:
          queue.append(current.left)
      if current.right:
          queue.append(current.right)
    return result


def main():
    #root = None
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
  
    print(traverse(root))

if __name__ == '__main__':
    main()