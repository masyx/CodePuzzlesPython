
from typing import List

# O(n) time | O(n) space
def missing_number(nums: List[int]) -> int:
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
def missing_number_2(nums):
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


def main():
    arr = [0, 1] 
    print(missing_number_2(arr))
    
    
if __name__ == "__main__":
    main()