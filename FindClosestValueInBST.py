class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space 
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target)

def findClosestValueInBstHelper(tree, target, closest = float('inf')):
    if tree is None:
        return closest
    if abs(target - tree.value) < abs(target - closest):
        closest = tree.value
    
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest
    
# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space    
def findClosestValueInBstRecursive(tree, target):
    return findClosestValueInBstRecursiveHelper(tree, target, float('inf'))

def findClosestValueInBstRecursiveHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - currentNode.value) < abs(target - closest):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


        
        


def main():
    tree = BST(10)
    # tree.left = BST(5)
    tree.right = BST(13)
    
    # tree.left.left = BST(2)
    # tree.left.right = BST(5)
    
    # tree.left.left.left = BST(1)
    
    # tree.right.left = BST(13)
    # tree.right.right = BST(22)
    
    # tree.right.left.right = BST(14)
    print(findClosestValueInBstRecursive(tree, 12))
    
    
if __name__ == "__main__":
    main()