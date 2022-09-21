class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

def find_level_averages(root):
    return


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))
    
    
if __name__ == "__main__":
    main()