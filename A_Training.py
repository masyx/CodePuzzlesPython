import math
from typing import List


class Solution:
    #  0  1  3  4  5  6
    # [0  1 45 46 46 47]
    # l = 0, r = 1, same_count = 1
    # w = 2, diff = 1
    
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        curr = 1
        best = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 0:
                continue
            elif nums[i] - nums[i - 1] == 1:
                curr += 1
            else:
                curr = 1
            
            if curr > best:
                best = curr

        return best
                



                    
    
def main():
    # [0, 10, 45, 46, 46, 47]
    nums = [0, 10, 45, 46, 46, 47]#[0,3,7,2,5,8,4,6,0,1] #[100,4,200,1,3,2]
    sol = Solution()
    print(sol.longestConsecutive(nums))
  
  
if __name__ == "__main__":
    main()