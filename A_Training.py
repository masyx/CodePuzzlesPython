'''
         1
       /   \
      2     3
     /\     /\
    4  5   6  7
   /      / \
  8      9  10


Preorder traversal: [1, 2, 4, 8, 5, 3, 6, 9, 10, 7]
Inorder traversal: [8, 4, 2, 5, 1, 9, 6, 10, 3, 7]
Postorder traversal: [8, 4, 5, 2, 9, 10, 6, 7, 3, 1]
'''

class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
        
def preorder_traversal(root, result: list):
    if root:
        result.append(root.value)
        preorder_traversal(root.left, result)
        preorder_traversal(root.right, result)
    return result

def inorder_traversal(root: Node, result: list):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.value)
        inorder_traversal(root.right, result)
    return result

def postorder_traversal(root: Node, result: list):
    if root:
        postorder_traversal(root.left, result)
        postorder_traversal(root.right, result)
        result.append(root.value)
    return result


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.right.left.left = Node(9)
    root.right.left.right = Node(10)
    
    print(f"Preorder traversal: {preorder_traversal(root, [])}")
    print(f"Inorder traversal: {inorder_traversal(root, [])}")
    print(f"Postorder traversal: {postorder_traversal(root, [])}")