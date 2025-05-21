from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(pos: int, path: List[int], sum_: int):
            if sum_ == target:
                result.append(path.copy())
                return
            
            for i in range(pos, len(nums)):
                if sum_ + nums[i] > target:
                    return
                path.append(nums[i])
                backtrack(i, path, sum_ + nums[i])
                path.pop()
        
        backtrack(0, [], 0)
        return result

    
    
def main():
    nums = [3]
    target = 3
    
    sol = Solution()
    print(sol.combinationSum(nums, target))
    
if __name__ == "__main__":
    main()