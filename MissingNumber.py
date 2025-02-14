"""268. Missing Number

Easy
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

 
Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.
                                  
Constraints: 
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""

from typing import List

# O(n) time | O(n) space
def missing_number_brute_force(nums: List[int]) -> int:
    # The input array contains distinct numbers in the range [0, n].
    # To ensure we check for the missing number across the full range,
    # we iterate from 0 to len(nums) (inclusive) by using range(len(nums) + 1).
    # For example, for the array [3, 0, 1] (length 3), range(3) would only cover 0, 1, and 2.
    # Using range(4) ensures that we also check if 3 is missing.
    all_nums = len(nums) + 1 
    nums_set = set(nums)
    
    for num in range(all_nums):
        if num not in nums_set:
            return num
 
# O(n log n) time | O(1) space       
def missing_number_brute_force_2(nums):
    nums.sort()
    
    if nums[-1] != len(nums): # Ensure that n is at the last index
        return len(nums)
    elif nums[0] != 0: # Ensure that 0 is at the first index
        return 0
    
    all_nums = len(nums)
    for i in range(all_nums):
        expected_num = i
        if expected_num != nums[i]:
            return expected_num

"""Finds the missing number in an array using XOR
This function finds the missing number in an array using XOR.
The problem: Given an array of n distinct numbers taken from the range [0, n],
where one number is missing, identify that missing number.
Key points and tricks in the solution:
1. Complete Range Inclusion:
   - The full range of expected numbers is [0, 1, 2, ..., n]. The array length is n,
     meaning one number from this range is missing.
   - We initialize `missing` with `n` because the array indices only cover 0 to n-1.
     This ensures that the number n is included in the XOR process.
2. XOR Properties:
   - XOR of a number with itself is 0 (e.g., a ^ a = 0).
   - XOR of a number with 0 remains unchanged (e.g., a ^ 0 = a).
   - The XOR operation is both commutative and associative, so the order of operations doesn't matter.
3. Pairwise Cancellation:
   - By iterating over the array with indices (using enumerate), each index i represents
     an expected number in the range [0, n-1].
   - In the loop, for each index i and array element num, we perform:
        missing ^= i ^ num
     This effectively XORs all expected numbers (via indices) and all actual numbers from the array.
   - Numbers that appear in both the complete range and the array cancel each other out,
     leaving the missing number as the final result.
4. Final Outcome:
   - After processing the entire array, `missing` holds the missing number.
This approach works efficiently in O(n) time and uses O(1) extra space.
"""
def missing_number(nums):
    missing = len(nums) # Start with n to include the number n, which isn't covered by the indices [0, n-1]
    for i, num in enumerate(nums):
        missing = missing ^ i ^ num # XOR both the index (expected number) and the value in the array
    return missing
    
def main():
    arr = [0, 1] 
    print(missing_number(arr))
    
    
if __name__ == "__main__":
    main()