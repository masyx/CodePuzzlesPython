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


    
    
if __name__ == "__main__":
    main()
        