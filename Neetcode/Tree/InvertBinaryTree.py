from collections import deque

class TreeNode:
    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

'''
Original:
    1
   / \
  2   3
 / \ / \
4  5 6  7

Inverted:
    1
   / \
  3   2
 / \ / \
7  6 5  4

'''
# O(n) time | space for call stack O(log n) balanced binary tree
#               O(n) for unbalanced tree (completely skewed, LinkedList) 
def invert_binary_tree1(root):
    if not root:
        return
    invert_binary_tree1(root.left)
    invert_binary_tree1(root.right)
    root.left, root.right = root.right, root.left
    return root

# O(n) time | extra space for queue: O(log n) balanced binary tree
# O(n)  unbalanced binary tree (completely skewed, LinkedList) 
def invert_binary_tree_iterative_queue(root: TreeNode):
    queue = deque([root])
    while queue:
        node = queue.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root

# O(n) time | extra space for stack: O(log n) balanced binary tree
# O(n)  unbalanced binary tree (completely skewed, LinkedList)
def invert_binary_tree_iterative_stack(root: TreeNode):
    stack = [root]
    while stack:
        current_node = stack.pop()
        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)
        current_node.left, current_node.right = current_node.right, current_node.left
    return root

def print_in_order(node):
    if not node:
        return
    print_in_order(node.left)
    print(node.value, end=' ')
    print_in_order(node.right)
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print("Original: ")
    print_in_order(root)
    
    print("\nInverted: ", )
    print_in_order(invert_binary_tree1(root))
    
    # Checking iterative solution
    print("\n\nIterative solution")
    invert_binary_tree_iterative_stack(root)
    print("Original: ")
    print_in_order(root)
    
    print("\nInverted: ", )
    print_in_order(invert_binary_tree_iterative_stack(root))
    
    
    
'''
Claude explanation

Q: Explain log n time complexity

A: Let's dive into this concept in detail, breaking it down step-by-step and using ASCII graphics to illustrate.

1. Balanced Binary Tree:
A balanced binary tree is a binary tree structure in which the depth of the left and right subtrees 
of every node differ by no more than one. This balance ensures that the tree doesn't become skewed, 
maintaining efficient operations.

Here's an ASCII representation of a balanced binary tree:

```
         4
       /   \
      2     6
     / \   / \
    1   3 5   7
```

2. Tree Depth and log n:
The depth of a tree is the number of edges from the root to the deepest leaf node. 
In a balanced binary tree with n nodes, the depth is approximately log₂n. Here's why:

- At each level, the number of nodes doubles (in a full binary tree).
- Level 0 (root): 2⁰ = 1 node
- Level 1: 2¹ = 2 nodes
- Level 2: 2² = 4 nodes
- ...
- Level d: 2ᵈ nodes

If we have n total nodes, we can express this as:
n ≈ 2ᵈ
Taking the log of both sides:
log₂n ≈ d
This is why we say the depth is approximately log₂n.

3. Log n Time Complexity:
Log n time complexity means that the time taken by an algorithm increases logarithmically
with the input size. In the context of a balanced binary tree, many operations (like search, insert, delete) 
have a time complexity of O(log n) because:

- At each step, we eliminate half of the remaining nodes.
- The maximum number of steps is equal to the depth of the tree.
- As we've seen, the depth is approximately log₂n.

Let's visualize this with an ASCII tree and a search operation:

```
         8             Step 1: Compare with root (8)
       /   \
      4    12          Step 2: Go left or right (eliminate half)
     / \   / \
    2   6 10 14        Step 3: Another comparison (eliminate half again)
   / \
  1   3               Step 4: Final comparison

Steps taken = depth of tree = log₂n (approx.)
```

4. Space Complexity and Recursion Stack:
When we perform recursive operations on a tree (like depth-first search), we use a call stack.
Each recursive call adds a new frame to this stack. The maximum depth of this stack is equal
to the height of the tree.

ASCII representation of the recursion stack for the leftmost branch:

```
   Stack:   | 1 |
            | 2 |
            | 4 |
            | 8 |
   Bottom    ---
```

Since the height of a balanced binary tree is O(log n), the maximum space used by the recursion 
stack is also O(log n).

5. Why This Matters:
The O(log n) space complexity is significantly better than O(n) for large datasets. For example:

- For n = 1,000,000:
  - O(n) = 1,000,000
  - O(log n) ≈ 20 (log₂1,000,000 ≈ 19.93)

This means that for a balanced tree with a million nodes, the maximum recursion depth (and thus space complexity)
is around 20, which is much more manageable than 1,000,000.

In conclusion, the balanced nature of the tree ensures that operations maintain 
logarithmic time and space complexity, making balanced binary trees efficient data structures for
many applications, especially when dealing with large datasets.
Would you like me to explain or elaborate on any specific part of this explanation?


ITERATIVE time complexity analysis:

Let's analyze the space complexity of an iterative implementation of the invert binary tree problem.
For an iterative approach to inverting a binary tree, we typically use a queue or a stack to keep track of nodes.
Let's consider both approaches:

1. Using a Queue (Breadth-First Approach):
In this approach, we process the tree level by level.

```
Algorithm:
1. Create a queue and enqueue the root
2. While the queue is not empty:
   a. Dequeue a node
   b. Swap its left and right children
   c. Enqueue the left and right children (if they exist)
```

Space Complexity Analysis:
- The maximum space used will be when the queue contains all nodes at the widest level of the tree.
- In a balanced binary tree, the widest level is the last level, which can contain up to n/2 nodes 
(where n is the total number of nodes).
- Therefore, the space complexity is O(n) in the worst case.

2. Using a Stack (Depth-First Approach):
This approach processes the tree in a depth-first manner.

```
Algorithm:
1. Create a stack and push the root
2. While the stack is not empty:
   a. Pop a node
   b. Swap its left and right children
   c. Push the right child, then the left child (if they exist)
```

Space Complexity Analysis:
- The maximum space used will be when the stack contains nodes along the height of the tree.
- In a balanced binary tree, the height is log(n).
- Therefore, the space complexity is O(log n) in the average case for a balanced tree.
- However, in the worst case (a completely unbalanced tree), it could still be O(n).

Comparison with Recursive Approach:

Recursive:
- Space: O(log n) for balanced trees, O(n) for worst-case unbalanced trees
- This space is used implicitly by the call stack

Iterative:
- Queue: O(n) in all cases
- Stack: O(log n) for balanced trees, O(n) for worst-case unbalanced trees
- This space is used explicitly by the data structure we choose

Key Points:
1. The iterative approach with a stack has the same space complexity as the recursive approach.
2. The iterative approach with a queue uses more space (O(n)) but processes the tree level by level.
3. The iterative approaches have explicit control over the space used, which can be an advantage in memory-constrained environments.

ASCII Illustration of Space Usage:
```
Balanced Tree:        Unbalanced Tree:

     4                     1
   /   \                    \
  2     6                    2
 / \   / \                    \
1   3 5   7                    3
                                \
                                 4

Stack/Recursion:     Stack/Recursion:
   |4|                  |1|
   |2|                  |2|
   |1|                  |3|
                        |4|

Queue (max):          Queue (max):
|1|3|5|7|              |4|
```

In conclusion, while the recursive and iterative (with stack) approaches have the same
theoretical space complexity, the iterative approach gives more explicit control over memory usage.
The queue-based approach, while using more space, can be advantageous for level-order processing of the tree.
'''
