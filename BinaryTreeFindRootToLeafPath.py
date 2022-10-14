'''Given a binary tree and a number sequence, find if the sequence is present as 
a root-to-leaf path in the given tree.'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n^2) time | O(d) space or O(n) in worst case
def find_path_2(root, sequence):
    result = []
    find_path_recursive(root, sequence, result)
    if result:
        return True
    else:
        return False

def find_path_recursive(root, sequence, result, current = []):
    if root is not None:
        current.append(root.val)
        find_path_recursive(root.left, sequence, result)
        find_path_recursive(root.right, sequence, result)
        if current == sequence:
            result.append(f"Found sequence: {sequence}")
        del current[-1]

# O(n) time | O(n) space in worst case when a binary tree is a linked list
def find_path(root, sequence):
    if root is None:
        return False
    return find_path_rec(root, sequence, 0)

def find_path_rec(node, sequence, seq_idx):
    if node is None:
        return False
    if seq_idx > len(sequence) - 1 or sequence[seq_idx] != node.val:
        return False
    elif seq_idx == len(sequence) - 1 and node.left is None and node.right is None:
        return True
        #return find_path_rec(node.left, sequence, seq_idx + 1) or \
    #    find_path_rec(node.right, sequence, seq_idx + 1)
    l = find_path_rec(node.left, sequence, seq_idx + 1)
    r = find_path_rec(node.right, sequence, seq_idx + 1)
    return l or r


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    
    #root.left.left.left = TreeNode(2)
    
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    #print("Tree has path sequence: " + str(find_path(root, [1, 0, 1])))
    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
    print("")


main()