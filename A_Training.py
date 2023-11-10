from typing import List
class Solution:
    def threeSum(self, nums: List[int], target) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                if nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                if nums[i] + nums[j] + nums[k] < target:
                    j += 1
        return result if result else None
            
def main():
    list1 = [8, 1, 10, 1, 2, 4]
    print(Solution().threeSum(list1, 11))


if __name__ == "__main__":
    main()