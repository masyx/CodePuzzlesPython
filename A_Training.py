from typing import List, Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {nums[0] : 0}
        
        for i in range(1, len(nums)):
            possible_match = target - nums[i]
            if possible_match in seen:
                return [seen[possible_match], i]
            seen[nums[i]] = i
        return None
    
    
    
def main():
  nums = [2,7,11,15]
  target = 26
  
  sol = Solution()
  print(sol.twoSum(nums, target))
  
  
if __name__ == "__main__":
    main()