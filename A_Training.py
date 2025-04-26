from typing import List
class SolutionBitManipulation:
    def hammingWeight_bf(self, n: int) -> int:
        count = 0
        for i in range(32):
            if 1 & (n >> i) != 0:
                count += 1
        return count
    
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
    
    def reverse_bits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n >> i
            res |= bit << (31 - i)
        return res
    
    def missing_number(self, nums):
        max_possible_missing = len(nums)
        res = max_possible_missing
        for i, num in enumerate(nums):
            res = res ^ i ^ num
        return res
    
    #   3 ->  11
    #   5 -> 101
    # res   
    #   1 ->  01
    #   1 ->  01
    # res      0
    #
    #
    def get_sum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        MAX_INT = 2 ** 31 - 1 # 0x7FFFFFFF
        
        while b:
            sum = a ^ b
            carry = (a & b) << 1
            a = sum & mask
            b = carry & mask
        return a if a <= MAX_INT else ~(a ^ mask)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
    
    @staticmethod
    def invert_tree_recursive(root: TreeNode):
        if not root:
            return
        if root.left:
            Solution.invert_tree_recursive(root.left)
        if root.right:
            Solution.invert_tree_recursive(root.right)
        root.left, root.right = root.right, root.left
        return root
    
    @staticmethod
    def invert_tree_iterative(root: TreeNode):
        if not root:
            return None
        stack = [root]
        while stack:
            current = stack.pop()
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            current.left, current.right = current.right, current.left
        return root
    
    @staticmethod
    def max_depth(root: TreeNode) -> int:
        if not root:
            return 0
        
        left = Solution.max_depth(root.left)
        right = Solution.max_depth(root.right)
        max_depth = max(left, right) + 1
        return max_depth
        
def main():
    # Creating a simple binary tree manually
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    # root.left.left.left = TreeNode(8)
    # root.left.left.right = TreeNode(9)
    # root.left.right.left = TreeNode(10)

    #Solution.invert_binary_tree(root)
    print(Solution.max_depth(root))
    
    
    # Visual representation of the tree:
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    #   / \ /
    #  8  9 10
    
    
if __name__ == "__main__":
    main()
        