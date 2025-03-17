
# nums = [-1,0,1,2,-1,-4] [-1,-1,-1,10,-9,0,1,2] -> [-1, -1, 2],skip [-1, -1, 2], [-1, 10, -9]

# O(n log n) time | O(n) space
from typing import List


def three_sum(nums):
    result = set()
    nums.sort()
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if curr_sum == 0:
                if (nums[i], nums[l], nums[r]) not in result:
                    result.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif curr_sum > 0:
                r -= 1
            else:
                l += 1
    return [list(i) for i in result]

def three_sum_neetcode(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, num in enumerate(nums):
        if num > 0:
            break

        if i > 0 and num == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = num + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([num, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                    
    return res
            
    

def main():
    nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
    #nums = [0,0,0]
    print(three_sum_neetcode(nums))
    
     
if __name__ == "__main__":
    main()