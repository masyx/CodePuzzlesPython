class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


# O(n) time | O(n) space
def has_path(root, sum, current_sum = 0):
    if root is None:
        return False
    current_sum += root.val
    if current_sum == sum:
        return True
    return has_path(root.left, sum, current_sum) or has_path(root.right, sum, current_sum)


def DFS(root, result = []):
    result.append(root.val)
    if root.left is not None:
        DFS(root.left, result)
    if root.right is not None:
        DFS(root.right, result)
    return result

def DFS_stack(root, result = []):
    stack = []
    stack.append(root)
    while stack:
        current = stack.pop()
        result.append(current.val)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return result


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))
  #print(DFS(root))


if __name__ == "__main__":
    main()