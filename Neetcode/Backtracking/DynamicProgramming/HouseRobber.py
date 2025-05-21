from typing import List


class Solution:
    # nums = [2,9,8,3,6,5,10]
    # i:     0  1  2   3
    # nums [10, 2, 1, 10]
    """
                           [0]
                           10?
                    /              \
                skip               rob(10)
                [1]                [2]
                2?                 1?
            /    \                  /      \
        [2]     [3]            [3]       [4] (out of bounds)
        1?      10?            10?        0
        / \     / \            / \
      [3] [4] [4] X          [4] X
      10? 0   0              0
    / \
    X   X

    
    
    """
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(i):
            if i > len(nums) - 1:
                return 0
            if cache[i] != -1:
                return cache[i]
            
            l = dfs(i + 1)
            r = dfs(i + 2) + nums[i]
            max_ = max(l, r)
            cache[i] = max_
            return max_
        return dfs(0)
        
        
def main():
    nums=[10, 8, 1, 10]
    sol = Solution()
    print(sol.rob(nums))


    
    
if __name__ == "__main__":
    main()