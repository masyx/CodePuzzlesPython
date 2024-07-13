# O(n log n) time | O(1) space
def containsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

# O(n) time | O(n) space
def containsDuplicate_2(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

    
    
if __name__ == "__main__":
    nums = [11, 3, 50, 11]
    print(containsDuplicate(nums))
    print(containsDuplicate_2(nums))
    