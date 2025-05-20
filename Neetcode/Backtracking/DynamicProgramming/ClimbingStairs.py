'''
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:
1 <= n <= 45
'''

class Solution:
    # Brute Force: O(2^n) time |O(n) space
    def climbStairs_BF(self, n: int) -> int:
        
        def cs_dfs(count):
            if count == n:
                return 1
            if count > n:
                return 0
            return cs_dfs(count + 1) + cs_dfs(count +2)
        
        return cs_dfs(0)
    
    def climbStairs_BF_2(self, n: int) -> int:
        
        def dfs(i):
            if i >= n:
                return i == n
            # In Python, True == 1 and False == 0, so boolean values can be added like integers
            return dfs(i + 1) + dfs(i + 2)
        
        return dfs(0)

    # O(n) time | O(n) space
    def climbStairs_DP_topDown(self, n):
        cache = [-1] * n
        def dp(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if cache[i] != -1:
                return cache[i]
            l = dp(i + 1)
            r = dp(i + 2)
            cache[i] = l + r
            return cache[i]
        
        return dp(0)
    
    def climbStairs(self, n):
        one, two = 0, 1
        
        for i in range(n):
            third = one + two
            one = two
            two = third 
        return (one, two)
        
        
def main():
    sol = Solution()
    print(sol.climbStairs_BF(8))
    print(sol.climbStairs_BF_2(8))
    print(sol.climbStairs_DP_topDown(8))
    print(sol.climbStairs(1))
    print(sol.getNthFib(8))

    
    
if __name__ == "__main__":
    main()
        