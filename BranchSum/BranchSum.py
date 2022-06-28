# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(n) space
def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums
    
    
def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return 
    
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return 
    
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)
    
        
            
    

def main():
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)
    
    tree.left.left.left = BinaryTree(8)
    tree.left.left.right = BinaryTree(9)
    
    tree.right.left = BinaryTree(6)
    tree.right.right = BinaryTree(7)
    
    print(branchSums(tree))
    
    
    
if __name__ == "__main__":
    main()
