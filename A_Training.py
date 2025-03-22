from typing import List


class Solution:
    
    """
    i              0  1 2  3
    nums:         [3, 8,2, 1]
    left_product: [1, 3,24,48]
    right_product:[16,2,1, 1]
    result:       [16,6,24,48]
    
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        n = len(nums)
        res = [0] * n
        left_product = [1] * n
        right_product = [1] * n
        
        for i in range(1, n):
            left_product[i] = nums[i - 1] * left_product[i - 1]
        for i in range(n - 2, -1, -1):
            right_product[i] = nums[i + 1] * right_product[i + 1]
            
        for i in range(n):
            res[i] = left_product[i] * right_product[i]
        
        return res

def main():
    nums = [3,8,2,1]
    s = Solution()
    print(s.productExceptSelf(nums))
    
     
if __name__ == "__main__":
    main()