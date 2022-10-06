"""Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. 
Find the total sum of all the numbers represented by all paths."""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n) time | O(n) space 
"""The space complexity of the above algorithm will be O(N) in the worst case. 
This space will be used to store the recursion stack. 
The worst case will happen when the given tree is a linked list (i.e., every node has only one child)."""
def find_sum_of_path_numbers_2(root):
    all_paths = []
    find_sum_of_path_numbers_helper_2(root, '', all_paths)
    return sum(all_paths)

def find_sum_of_path_numbers_helper_2(root, current_number, all_paths):
    if root is None:
        return
    current_number += str(root.val)
    if root.left is None and root.right is None:
        all_paths.append(int(current_number))
    find_sum_of_path_numbers_helper_2(root.left, current_number, all_paths)
    find_sum_of_path_numbers_helper_2(root.right, current_number, all_paths)


# O(n) time | O(n) space 
def find_sum_of_path_numbers(root):
    return find_sum_of_path_numbers_helper(root, 0)

def find_sum_of_path_numbers_helper(root, path_sum):
    if root is None:
        return 0
    path_sum = path_sum * 10 + root.val
    if root.left is None and root.right is None:
        return path_sum
    left = find_sum_of_path_numbers_helper(root.left, path_sum)
    right = find_sum_of_path_numbers_helper(root.right, path_sum)
    return left + right

def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers_2(root)))


main()