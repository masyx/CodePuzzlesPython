"""136. Single Number
Easy

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.
"""

""" XOR Operation and its Application: Leetcode 136 - Single Number

Definition:
XOR (⊕) is a bitwise operation that compares each bit of two binary numbers:
  - 1 ⊕ 1 = 0, 0 ⊕ 0 = 0 (bits are the same → 0)
  - 1 ⊕ 0 = 1, 0 ⊕ 1 = 1 (bits are different → 1)

Key Properties:
1. Identity: a ⊕ 0 = a (XOR with 0 does nothing).
2. Self-Inverse: a ⊕ a = 0 (XORing a number with itself cancels it).
3. Commutative: a ⊕ b = b ⊕ a (order doesn’t matter).
4. Associative: (a ⊕ b) ⊕ c = a ⊕ (b ⊕ c) (grouping doesn’t matter).

Why XOR Works for Finding Unique Numbers:
- XOR cancels out duplicates because of the self-inverse property (a ⊕ a = 0).
- XOR with 0 does not affect the number (a ⊕ 0 = a).
- Using commutative and associative properties, we can XOR numbers in any order to isolate the unique number.

Example:
Array: [1, 2, 2]
1. result = 0
2. result ⊕ 1 = 1
3. result ⊕ 2 = 3
4. result ⊕ 2 = 1
Final result = 1 (the unique number).
"""



from collections import defaultdict
from typing import List

def single_number_1(nums: List[int]):
    seen = {}
    for num in nums:
        if num in seen:
            del seen[num]
        else:
            seen[num] = 1
    key, value = seen.popitem()
    return key

def single_number_2(nums: List[int]):
    numbers = defaultdict(int)
    for num in nums:
        numbers[num] += 1
    
    for number in numbers:
        if numbers[number] == 1:
            return number

# O(n) time | O(1) space
def single_number(nums: List[int]):
    result = 0
    for num in nums:
        result ^= num # XOR each number with the result
    return result

if __name__ == "__main__":
    nums = [1,2,1,3,3]
    print(single_number_2(nums))