from typing import Optional
from collections import deque

class Solution:
    
    def hammingWeight_bf(self, n: int) -> int:
        counter = 0
        mask = 1
        for i in range(32):
            if n & mask != 0:
                counter += 1
            mask = mask << 1
        return counter
    
    def hammingWeight(self, n):
        counter = 0
        while n:
            counter += 1
            n &= n - 1
        return counter
    
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = result | ( bit << (31 - i))
        return result
    
    def missingNumber(self, nums) -> int:
        res = len(nums)
        for i, n in enumerate(nums):
            res = res ^ n ^ i
        return res
    
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 2 ** 31
        while b:
            sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum
            b = carry
        return a if a <= max_int else ~(a ^ mask)
    # 1 - 001
    # 2 - 010
    # 3 - 011
    # 4 - 100
    # 5 - 101
    # 6 - 110
    # 7 - 111
        
# n = 3       
def main():
    n = 8
    sol = Solution()
    print(sol.hammingWeight_bf(n))
    print(sol.hammingWeight(n))
    
    print(sol.reverseBits(4))
    
    nums = [3, 0, 1]
    print(sol.missingNumber(nums))


    
    
if __name__ == "__main__":
    main()
        