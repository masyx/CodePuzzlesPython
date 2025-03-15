from typing import List

# [100,4,200,1,3,2] Output:4
def longest_consec_seq_bf(nums):
    longest_streak = 0

    for num in nums:
        current_num = num
        current_streak = 1

        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak

def longest_consec_seq_sort(nums: List):
    if not nums:
        return 0

    nums.sort()

    longest_streak = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

    return max(longest_streak, current_streak)


def main():
    nums = [100,4,200,1,3,2]
    print(longest_consec_seq_bf(nums))
    print(longest_consec_seq_sort([1,0,1,1,1,1,2]))

if __name__ == "__main__":
    main()