from typing import List


class Solution:
    # nums = [2,9,8,3,6,5,10]
    # nums = [1,1,1,10,1,10,10]
    def rob(self, nums: List[int]) -> int:
        max_money = 0
        for i in range(2):
            j = i
            curr_money = 0
            while j <= len(nums) - 1:
                curr_money += nums[j]
                j += 2
            max_money = max(max_money, curr_money)
        return max_money
        
        
def main():
    nums=[5,1,2,10,6,2,7,9,3,1]
    sol = Solution()
    print(sol.rob(nums))


    
    
if __name__ == "__main__":
    main()