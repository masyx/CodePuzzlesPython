from typing import List
from collections import defaultdict

class Solution:
    # O(n^2) space | O(n) space
    def minimumOperations(self, nums: List[int]) -> int:
        def is_unique(start) -> bool:
            seen = set()
            for num in nums[start:]:
                if num in seen:
                    return False
                seen.add(num)
            return True
        
        res = 0
        for i in range(0, len(nums),  3):
            if not is_unique(i):
                res += 1
        return res
    #   i:    0 1 2 3 4 5 6 7 8
    #nums:   [1,2,3,4,2,3,3,5,7]
    def min_operations(self, nums):
        res = 0
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                res = i // 3 + 1
                break
            seen.add(nums[i])
        return res
        
    
def main():
    nums = [1,2,3,4,2,3,3,5,7]
    nums = [3,3,3,3,3,3]
    # nums = [1,2,3,4,5,6,7,8,9,10]
    solution = Solution()
    print(solution.minimumOperations(nums))
    print(solution.min_operations(nums))
    
    
     
if __name__ == "__main__":
    main()
        