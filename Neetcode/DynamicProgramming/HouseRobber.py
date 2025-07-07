"""198. House Robber
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it 
will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob 
tonight without alerting the police.

 
Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

from typing import List


class Solution:
    # i:     0  1  2   3
    # nums [10, 2, 1, 10]
    # O(n) time | O(n) space
    def rob_recursive_topDown(self, nums):
        cache = [-1] * len(nums)
        def best(i):
            if i >= len(nums):
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            rob_house = nums[i] + best(i + 2)
            skip_house = best(i + 1)
            
            cache[i] = max(rob_house, skip_house)
            return cache[i]
    
    """
    House Robber - Bottom-Up DP

    Idea:
    - Let dp[i] = max money you can rob from house 0 to i.
    - At each house, you either:
        - Rob it → add nums[i] to dp[i-2]
        - Skip it → carry over dp[i-1]
    - Recurrence: dp[i] = max(dp[i-1], nums[i] + dp[i-2])

    Base cases:
    - dp[0] = nums[0]
    - dp[1] = max(nums[0], nums[1])
    """
    # O(n) time | O(n) space
    def rob_DP_bottomUp(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        
        # dp[i] - the max amount you can rob from house 0 up to house i
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            skip_house = dp[i - 1]
            rob_house = nums[i] + dp[i - 2]
            dp[i] = max(skip_house, rob_house)
            
        return dp[n-1]
        
    def rob_recursive_topDown(self, nums):
        cache = [-1] * len(nums)
        def best(i):
            if i >= len(nums):
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            rob_house = nums[i] + best(i + 2)
            skip_house = best(i + 1)
            
            cache[i] = max(rob_house, skip_house)
            return cache[i]
        
        return best(0)
    
    """
    House Robber - Space-Optimized DP

    Track only the last two results:
    - prev1 = max money up to previous house
    - prev2 = max money up to house before that

    For each house:
    - Either rob it → num + prev2
    - Or skip it → prev1
    Update: curr = max(prev1, num + prev2)

    Time: O(n)
    Space: O(1)
    """       
    def rob(nums):
        prev2 = 0  # This represents dp[i - 2] → max money if we skip the last house
        prev1 = 0  # This represents dp[i - 1] → max money if we consider up to the last house

        for num in nums:
            # Either skip this house → prev1,
            # or rob it → num + prev2
            curr = max(prev1, num + prev2)

            # Shift the variables for the next iteration
            prev2 = prev1
            prev1 = curr

        return prev1  
        
        
def main():
    nums=[10, 8, 1, 3, 11]
    sol = Solution()
    print(sol.rob_DP_bottomUp(nums))
    print(sol.rob_recursive_topDown(nums))


    
    
if __name__ == "__main__":
    main()