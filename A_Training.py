from typing import Optional
from collections import deque

class Solution:
    
    # [1,5,3,8,50,9,6,9]
    def houseRobber(self, nums):
        cache = [-1] * len(nums)
        
        def best(i):
            if i >= len(nums):
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            explore_hose = nums[i] + best(i + 2)
            skip_hose = best(i + 1)
            
            cache[i] = max(explore_hose, skip_hose)
            return cache[i]
        
        return best(0)

          

# n = 3       
def main():
    # i:      0 1 2   3
    nums = [100,5,3,200]
    sol = Solution()
    print(sol.houseRobber(nums))


    
    
if __name__ == "__main__":
    main()
        