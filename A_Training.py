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
                
def main():
    sol = SolutionBitManipulation()
    
    # region BitManipulation testing
    n = 2 ** 31 - 1 # 2147483647
    print(f"Number of set bits in '{n}' is: {sol.hammingWeight(n)}")
    print()
    
    n = 1
    print(f"Reversed '{n}' is: {sol.reverse_bits(n)}")
    print()
    
    nums = [3,0,1]
    print(f"Missing number in an array {nums} is: {sol.missing_number(nums)}")
    print()
    
    a, b = 3, 3
    print(f"Sum of {a} and {b} is: {sol.get_sum(a, b)}")
    
    # endregion

    nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    ums = [0,0,20,0,20,2,1]
    s = Solution()
    print(s.trap(nums))
    
    
if __name__ == "__main__":
    main()
        