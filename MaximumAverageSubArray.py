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
    def findMaxAverage_verbose(self, nums, k):
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

    def findMaxAverage(self, nums, k):
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum / k
    
    def find_max_average_cumulative_sum(self, nums, k):
        # Step 1: Create the cumulative sum array
        # cum_sum = [0]
        # for num in nums:
        #     cum_sum.append(cum_sum[-1] + num)
        cum_sum = [nums[0]]
        for i in range(1, len(nums)):
            cum_sum.append(cum_sum[-1] + nums[i])

        # Step 2: Find the maximum sum of a subarray of length k
        max_sum = cum_sum[k - 1]  # Initial maximum sum of the first 'k' elements
        for i in range(k, len(nums)):
            current_sum = cum_sum[i] - cum_sum[i - k]
            max_sum = max(max_sum, current_sum)

        # Step 3: Calculate the maximum average
        return max_sum / k


def main():
    nums = [1,12,-5,-6,50,3]
    print(Solution().find_max_average_cumulative_sum(nums, 4))
    
    
if __name__ == "__main__":
    main()