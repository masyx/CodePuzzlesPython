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

if __name__ == "__main__":
    nums = [1,2,1,3,3]
    print(single_number_2(nums))