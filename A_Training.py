from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k) -> int:
        l = 0
        kSum = sum(nums[:k])
        max_average = kSum / k
        
        for r in range(k, len(nums)):
            kSum -= nums[l]
            kSum += nums[r]
            curr_average = kSum / k
            max_average = max(max_average, curr_average)
            l += 1
        
        return max_average

            
def main():
    list1 = [0,4,0,3,2]
    print(Solution().findMaxAverage(list1, 1))


if __name__ == "__main__":
    main()