""" You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average 
value and return this value. Any answer with a calculation 
error less than 10-5 will be accepted. """

"""
Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

class Solution:
    # O(n) time | O(1) space
    def findMaxAverage(self, nums, k):
        kSum = sum(nums[:k])
        l = 0
        max_average = kSum / k
        
        for r in range(k, len(nums)):
            kSum -= nums[l]
            kSum += nums[r]
            curr_average = kSum / k
            max_average = max(max_average, curr_average)
            l += 1
            
        return max_average


def main():
    nums = [1,12,-5,-6,50,3]
    print(Solution().findMaxAverage(nums, 4))
    
    
if __name__ == "__main__":
    main()