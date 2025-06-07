from typing import Optional
from collections import deque

class Solution:
    # Brute Force: O(2^n) time |O(log n) space
    def climbStairs(self, n: int) -> int:
        def climbStairsHelper(i):
            if i >= n:
                return i == n
            return climbStairsHelper(i + 1) + climbStairsHelper(i + 2)
            
        return climbStairsHelper(0)
    
    def climbStairsMemo(self, n):
        memo = {}
        def climbStairsHelper(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            if i in memo:
                return memo[i]
            
            
            l = climbStairsHelper(i + 1)
            r = climbStairsHelper(i + 2)
            memo[i] = l + r
            return memo[i]
        
        return climbStairsHelper(0)
        
        

# n = 3       
def main():
    sol = Solution()
    print(sol.climbStairs(4))
    print(sol.climbStairsMemo(4))

    
    
if __name__ == "__main__":
    main()
        