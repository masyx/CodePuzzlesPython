'''
35. Search Insert Position
Easy
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
'''

#   0  1  2  3  4
# [-1, 2, 4, 7, 9] target = 8
# l = 4, r = 4, mid = 3

def search_insert(nums, target):
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


if __name__ == "__main__":
    nums = [-1, 2, 4, 7, 9]
    target = 8
    print(search_insert(nums, target))