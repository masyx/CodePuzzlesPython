class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # O(log(n)) time average | O(log(n)) space
    # O(n) time worst | O(n) space   
    def insertRecursion(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                return BST.insert(self.right, value)
        else:
            if self.left is None:
                self.left = BST(value)
            else:
                return BST.insert(self.left, value)
    
    
    # O(log(n)) time average | O(1) space
    # O(n) time worst | O(1) space          
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self  # this return statement just for AlgoExpert testing purposes to
                     # be able to run insert function like  testBst.insert(5).insert(10)...   

    
    def remove(root, key):
        if not root: # if root doesn't exist, just return it
            return root
        if root.value > key: # if key value is less than root value, find the node in the left subtree
            root.left = BST.remove(root.left, key)
        elif root.value < key: # if key value is greater than root value, find the node in right subtree
            root.right= BST.remove(root.right, key)
        else: #if we found the node (root.value == key), start to delete it
            if not root.right: # if it doesn't have right children, we delete the node then new root would be root.left
                return root.left
            if not root.left: # if it has no left children, we delete the node then new root would be root.right
                return root.right
                # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
            temp = root.right
            mini = temp.value
            while temp.left:
                temp = temp.left
                mini = temp.value
            root.value = mini # replace value
            root.right = BST.remove(root.right,root.value) # delete the minimum node in right subtree
        return root
            
            
    # O(log(n)) time average | O(log(n)) space
    # O(n) time worst 
    def containsRecursion(self, value):
        if self == None:
            return False
        elif value == self.value:
            return True
        elif value < self.value:
            return BST.contains(self.left, value)
        elif value > self.value:
            return BST.contains(self.right, value)
        
    
    # O(log(n)) time average | O(1) space
    # O(n) time worst | O(1) space
    def contains(self, value):
        current_node = self
        while current_node is not None:
            if current_node.value == value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
    
    
    
def main():
    tree = BST(10)
    
    tree.insert(5)
    tree.insert(2)
    tree.insert(5)
    tree.insert(1)
    
    tree.insert(15)
    tree.insert(13)
    tree.insert(22)
    tree.insert(14)
    tree.insert(12)
    
    what = tree.contains(15)
    hh = tree.remove(5)
    print(what)
    
if __name__ == "__main__":
    main()