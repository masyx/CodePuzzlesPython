from typing import Optional
from collections import deque

class Solution:
    # Brute Force: O(2^n) time |O(log n) space
    def climbStairs(self, n: int) -> int:
        def cs_dfs(count):
            if count == n:
                return 1
            if count > n:
                return 0
            return cs_dfs(count + 1) + cs_dfs(count +2)
        return cs_dfs(0)


        
def main():
    sol = Solution()
    print(sol.climbStairs(4))

    
    
if __name__ == "__main__":
    main()
        