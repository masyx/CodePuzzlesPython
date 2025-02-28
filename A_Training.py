from typing import List

# O(n) time | O(n) space
def missing_number_bf(nums):
    seen = set()
    for num in nums:
        seen.add(num)
    for i in range(len(nums)):
        if i not in seen:
            return i
        
def missing_number(nums):
    max_possible_number = len(nums)
    res = max_possible_number
    for i in range(max_possible_number):
        res = res ^ i ^ nums[i]
    return res
    
    
if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    print(missing_number_bf(nums))
    print(missing_number(nums))
