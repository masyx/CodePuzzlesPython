class Solution:
    def firstDuplicateValue(self, nums: list[int]) -> bool:
        present = {}
        for num in nums:
            if num in present:
                return True
            present[num] = True
        return False
    


def main():
    array = [1,2,3,1]
    s = Solution()
    print(s.firstDuplicateValue(array))
    
    
if __name__ == "__main__":
    main()