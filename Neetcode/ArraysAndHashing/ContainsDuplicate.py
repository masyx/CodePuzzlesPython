'''217. Contains Duplicate
Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.


Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''

from typing import List

# [1,2,3,1]
# O(n) time | O(n) space
def contain_duplicate(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contain_duplicate_short(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

def main():
    nums = [1,2,3,1]
    print(contain_duplicate(nums))
    
    
if __name__ == "__main__":
    main()