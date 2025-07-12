from typing import Optional
from collections import deque

class Solution:
    
    # [1,5,3,8,50,9,6,9]
    def houseRobber_topDown(self, nums):
        cache = [-1] * len(nums)
        
        def best(i):
            if i >= len(nums):
                return 0
            
            skip_house = best(i + 1)
            rob_house = nums[i] + best(i + 2)
            
            cache[i] = max(skip_house, rob_house)
            
            return cache[i]
        return best(0)
    
    # [100,5,3,200]
    # [100,100, 103, 0]
    def houseRobber_bottomUp(self, nums):
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        best = [0] * len(nums)
        best[0] = 100
        best[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            skip_house = best[i - 1]
            rob_house = nums[i] + best[i - 2]
            best[i] = max(skip_house, rob_house)
        return best[-1]    

# n = 3       
def main():
    # i:      0 1 2   3
    nums = [100,5,3,200]
    sol = Solution()
    print(sol.houseRobber_topDown(nums))
    print(sol.houseRobber_bottomUp(nums))


    
    
if __name__ == "__main__":
    main()
        