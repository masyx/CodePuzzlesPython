from typing import List


class Solution:
    # nums = [2,10,7,3,7]
    # i:     0  1  2   3
    # nums [10, 2, 1, 10]
    """
                           [0]
                           10?
                    /              \
              skip [1]                rob(10)
                                  [2]
              2?                      1?
            /    \                  /    \
        [2]     [3]               [3]    [4] (out of bounds)
         1?     10?               10?     0
        / \     / \               / \
      [3] [4] [4]  X            [4]  X
      10?  0   0                 0
      / \
     X   X

    
    
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Create a dp table with 2 extra slots for base cases
        dp = [0] * (n + 2)

        print("Starting bottom-up DP computation:")
        print(f"nums = {nums}")
        print("-" * 40)

        # Step 2: Work from the end of the list to the beginning
        for i in range(n - 1, -1, -1):
            skip = dp[i + 1]  # case: skip current house
            rob_this = nums[i] + dp[i + 2]  # case: rob current house

            dp[i] = max(skip, rob_this)

            # Step-by-step explanation:
            print(f"At index {i} (House value = {nums[i]}):")
            print(f"  Option 1 - Skip:   dp[{i+1}] = {skip}")
            print(f"  Option 2 - Rob:    nums[{i}] + dp[{i+2}] = {nums[i]} + {dp[i+2]} = {rob_this}")
            print(f"  Choose max:        dp[{i}] = {dp[i]}")
            print("-" * 40)

        print(f"Final dp table: {dp[:n]}")
        print(f"Maximum money that can be robbed: {dp[0]}")
        return dp[0]

                
            
        
        
def main():
    nums=[10, 8, 1, 10]
    #nums = [2,10,7,3,7]
    sol = Solution()
    print(sol.rob(nums))


    
    
if __name__ == "__main__":
    main()