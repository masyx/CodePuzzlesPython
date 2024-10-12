'''
15. 3Sum
Medium
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

===Notice that the solution set must not contain duplicate triplets.===

 

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
'''
# i 0  1  2 3 4 5
# [-4,-1,-1,-1,0,1,2]
#

# Time and space complexity analysis
# sorting n log n
# iteration: two_sum run in O(n)(this is while loop) and we run in O(n) time(this is for loop), 
# so overall time complexity is O(n^2)
# O(n^2) time | O(n log n) space for sorting
def three_sum(numbers):
    if not numbers:
        return []
    result = []
    numbers.sort()
    for i, a in enumerate(numbers):
        if a > 0: # not possible to get 0 as a sum
            break
        if i != 0 and a == numbers[i - 1]: # avoiding duplicates in the result
            continue
        l = i + 1
        r = len(numbers) - 1
        while l < r:
            curr_numbers = [numbers[i], numbers[l], numbers[r]]
            curr_sum = sum(curr_numbers)
            if curr_sum > 0:
                r -= 1
            elif curr_sum < 0:
                l += 1
            else:
                result.append(curr_numbers)
                l += 1
                while l < r and numbers[l] == numbers[l - 1]:
                    l += 1
    return result




if __name__ == "__main__":
    numbers = [-1,0,1,2,-1,-4]
    #numbers = [-2,0,0,2,2] edge case for two_sum method
    print(three_sum(numbers))