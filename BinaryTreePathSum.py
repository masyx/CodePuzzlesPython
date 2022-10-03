class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# O(n) time | O(n) space
def has_path(root, sum):
    if root is None:
        return False
    if sum == root.val and root.left is None and root.right is None:
        return True
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)

# O(n) time | O(n) space
def has_path_2(root, sum, current_sum = 0):
    if root is None:
        return False
    current_sum += root.val
    if current_sum == sum and root.left is None and root.right is None:
        return True
    return has_path(root.left, sum, current_sum) or has_path(root.right, sum, current_sum)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


if __name__ == "__main__":
    main()