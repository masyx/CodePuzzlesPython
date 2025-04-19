from typing import List
class SolutionBitManipulation:
    def hammingWeight_bf(self, n: int) -> int:
        count = 0
        for i in range(32):
            if 1 & (n >> i) != 0:
                count += 1
        return count
    
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
    
    def reverse_bits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n >> i
            res |= bit << (31 - i)
        return res
    
    def missing_number(self, nums):
        max_possible_missing = len(nums)
        res = max_possible_missing
        for i, num in enumerate(nums):
            res = res ^ i ^ num
        return res
    
    #   3 ->  11
    #   5 -> 101
    # res   
    #   1 ->  01
    #   1 ->  01
    # res      0
    #
    #
    def get_sum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        MAX_INT = 2 ** 31 - 1 # 0x7FFFFFFF
        
        while b:
            sum = a ^ b
            carry = (a & b) << 1
            a = sum & mask
            b = carry & mask
        return a if a <= MAX_INT else ~(a ^ mask)
        
class Solution:
    def search_rotated(self, nums: List[int], target: int):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # left subarray is sorted
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right subarray is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
                
def main():
    sol = SolutionBitManipulation()
    
    # region BitManipulation testing
    n = 2 ** 31 - 1 # 2147483647
    print(f"Number of set bits in '{n}' is: {sol.hammingWeight(n)}")
    print()
    
    n = 1
    print(f"Reversed '{n}' is: {sol.reverse_bits(n)}")
    print()
    
    nums = [3,0,1]
    print(f"Missing number in an array {nums} is: {sol.missing_number(nums)}")
    print()
    
    a, b = 3, 3
    print(f"Sum of {a} and {b} is: {sol.get_sum(a, b)}")
    
    # endregion

    #  i    0 1 2 3 4 5 6 7 8 9
    nums = [5,6,7,8,9,0,1,2,3,4]
    s = Solution()
    print(s.search_rotated(nums, 8))
    
    
if __name__ == "__main__":
    main()
        