'''
Given an array of positive numbers, nums, such that the values lie in the range [1,n], inclusive, 
and that there are n+1 numbers in the array, find and return the duplicate number present in nums. 
There is only one repeated number in nums.

Note: You cannot modify the given array nums. You have to solve the problem using only constant extra space.
'''

# O(n) time | O(n) space
def find_duplicate_extra_space(nums):
    seen = {nums[0]}
    for i in range(1, len(nums)):
        if nums[i] in seen:
            return nums[i]
        seen.add(nums[i])
    return None


if __name__ == "__main__":
    nums = [1,3,4,2,2]
    print(find_duplicate(nums))