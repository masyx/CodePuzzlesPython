class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value): 
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
        return self
    
    def remove(self, value):
        # if value == self.value:
        #     del self
        # elif value > self.value:
        #     return BST.remove(self.right, value)
        # else:
        #     return BST.remove(self.left, value)
        return self
    
    def contain(self, value):
        if self == None:
            return False
        elif value < self.value:
            return BST.contain(self.left, value)
        elif value > self.value:
            return BST.contain(self.right, value)
        elif value == self.value:
            return True
    
    
    
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
    
    what = tree.contain(15)
    print(what)
    
if __name__ == "__main__":
    main()