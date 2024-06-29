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

def find_duplicate_my(nums):
    slow = nums[0]
    fast = nums[slow]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

def find_duplicate_sort(nums: list):
    nums.sort()
    for i, number in enumerate(nums):
        if number == nums[i - 1]:
            return number
    return None

def find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
    while fast != slow:
        slow = nums[slow]
        fast = nums[fast]
    return slow
    
    
if __name__ == "__main__":
    nums = [3,1,4,2,1]
    print(find_duplicate(nums))