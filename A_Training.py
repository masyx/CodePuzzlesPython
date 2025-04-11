from typing import List
from collections import defaultdict

class Solution:
    #nums:    [-1,0,1,2,-1,-4]
    #
    #   i:      0  1  2 3 4 5
    #nums:    [-4,-1,-1,0,1,2]
    # target = x + y + z => target - x = y + z => 0 - x = y + z => -x = y + z
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            curr_num = nums[i]
            if curr_num > 0:
                break
            if i > 0 and curr_num == nums[i - 1]:
                continue
            
            self.two_sum(i + 1, nums, -curr_num, res)
        return res
    # length = 3
    #       v
    #   0 1 2
    # [-2,1,1]
    # seen: 1
    def two_sum(self, start, nums, target, res):
        seen = set()
        i = start
        while i < len(nums):
            curr_num = nums[i]            
            compliment = target - curr_num
            if compliment in seen:
                res.append([nums[start - 1], compliment, curr_num])
                while i + 1 < len(nums) and curr_num == nums[i + 1]:
                    i += 1
            seen.add(curr_num)
            i += 1
        return res
        
        
    
def main():
    nums = [-1,0,1,2,-1,-4]
    nums = [0,0,0,0]
    solution = Solution()
    print(solution.threeSum(nums))
    
    
     
if __name__ == "__main__":
    main()
        