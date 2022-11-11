class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Same as findClosestValueInBst_Recursive, just have explicitly defined 
# closest variable for better understanding during debugging
def findClosestValueInBst_Recursive_2(tree, target, closest = float("inf")):
    if tree is None:
        return closest
    if abs(tree.value - target) < abs(closest - target):
        closest = tree.value
    if target > tree.value:
        closest = findClosestValueInBst_Recursive_2(tree.right, target, closest)
        return closest
    else:
        closest = findClosestValueInBst_Recursive_2(tree.left, target, closest)
        return closest

# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
def findClosestValueInBst_Recursive(tree, target, closest = float("inf")):
    if tree is None:
        return closest
    if abs(tree.value - target) < abs(closest - target):
        closest = tree.value
    if target > tree.value:
        return findClosestValueInBst_Recursive(tree.right, target, closest)
    else:
        return findClosestValueInBst_Recursive(tree.left, target, closest)
    
# O(log n) time | O(1) time
def findClosestValueInBst_Iterative(tree, target, closest = float("inf")):
    while tree:
        if abs(tree.value - target) < abs(closest - target):
            closest = tree.value
        if target > tree.value:
            tree = tree.right
        else:
            tree = tree.left
    return closest

def main():
    tree = BST(10)
    tree.left = BST(5)
    tree.right = BST(13)
    tree.left.left = BST(2)
    tree.left.right = BST(5)
    tree.left.left.left = BST(1)
    tree.right.left = BST(13)
    tree.right.right = BST(22)
    tree.right.left.right = BST(14)
    
    print(findClosestValueInBst_Iterative(tree, 23))


if __name__ == "__main__":
    main()