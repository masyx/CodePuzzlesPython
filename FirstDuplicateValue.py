class Solution:
    # O(n) time | O(n) space
    def firstDuplicateValue(self, nums: list[int]) -> bool:
        present = set()
        for num in nums:
            if num in present:
                return num
            present.add(num)
        return -1
    
    # O(n^2) time | O(1) space
    def firstDuplicateValueBruteForce(self, nums):
        min_second_index = len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    min_second_index = min(min_second_index, j)
        if min_second_index == len(nums):
            return - 1
        else:
            return nums[min_second_index]
        
    # O(n) time | O(1) space
    def firstDuplicateValue(self, array):
        for num in array:
            absValue = abs(num)
            if array[absValue - 1] <= 0:
                return absValue
            array[absValue - 1] *= -1
        return -1
        
    


def main():
    # [1,2,3,1] [0,-1, -2, 0]
    array = [2, 1, 5, 3, 3, 2, 4]
    s = Solution()
    print(s.firstDuplicateValueBruteForce(array))
    
    
if __name__ == "__main__":
    main()