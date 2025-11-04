from typing import List

# [100,4,200,1,3,2] Output:4
def longest_consec_seq_bf(nums):
    longest_streak = 0
    
    for i in range(len(nums)):
        current_streak = 1
        current_num = nums[i]
        while current_num + 1 in nums:
            current_streak += 1
            current_num += 1
        longest_streak = max(current_streak, longest_streak)
    return longest_streak

# O(n log n) time | O(n) space, for sorting in Python 
def longest_consec_seq_sort(self, nums: List[int]) -> int:
    if not nums:
        return 0

    # Sort numbers so consecutive values become neighbors
    nums.sort()
    best = 1   # longest sequence found so far
    curr = 1   # current consecutive streak length

    # Walk through sorted array and count streaks
    for i in range(1, len(nums)):
        # Skip duplicates; they don't break or extend a streak
        if nums[i] == nums[i-1]:
            continue
        # Consecutive: extend current streak
        if nums[i] == nums[i-1] + 1:
            curr += 1
        else:
            # Gap: reset streak to this single number
            curr = 1
        # Track the maximum streak length
        if curr > best:
            best = curr

    return best

''' Optimal solution explanation
This optimized algorithm contains only two changes from the brute force
approach: the numbers are stored in a HashSet (or Set, in Python) to
allow O(1) lookups, and we only attempt to build sequences from numbers
that are not already part of a longer sequence. This is accomplished by first
ensuring that the number that would immediately precede the current number in
a sequence is not present, as that number would necessarily be part of a
longer sequence.
'''
''' O(n) time | O(n) space, explanation -> 
Time complexity : O(n).

Although the time complexity appears to be quadratic due to the while
loop nested within the for loop, closer inspection reveals it to be
linear. Because the while loop is reached only when currentNum marks
the beginning of a sequence (i.e. currentNum-1 is not present in
nums), the while loop can only run for n iterations throughout the
entire runtime of the algorithm. This means that despite looking like
O(n⋅n) complexity, the nested loops actually run in O(n+n)=O(n)
time. All other computations occur in constant time, so the overall
runtime is linear.

Space complexity : O(n).

In order to set up O(1) containment lookups, we allocate linear space
for a hash table to store the O(n) numbers in nums. Other than that,
the space complexity is identical to that of the brute force solution.
'''
def longest_consec_seq(self, nums: List[int]) -> int:
    # Use a set for O(1) existence checks
    nums_set = set(nums)
    longest_streak = 0

    # # Treat only "sequence starts" (num-1 not in set) as anchors
    for num in nums_set:
        if num - 1 not in nums_set:  # num is the start of a sequence
            current_num = num
            current_streak = 0

            # Count how long this consecutive sequence goes
            while current_num in nums_set:
                current_streak += 1
                current_num += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

def longest_consec_seq_cleanest(self, nums: List[int]) -> int:
    # Use a set for O(1) existence checks
    s = set(nums)
    best = 0

    # Treat only "sequence starts" (x-1 not in set) as anchors
    for x in s:
        if x - 1 not in s:  # x is the beginning of a sequence
            y = x
            # Walk forward while numbers stay consecutive
            while y in s:
                y += 1
            # Length of this sequence is y - x
            best = max(best, y - x)

    return best


def main():
    nums = []
    #nums = [12,14,10,13,11,4,200,1,3,2]
    nums_2 = [1,0,1,1,1,1,2]
    print(longest_consec_seq_bf(nums))
    print(longest_consec_seq_sort(nums))
    print(longest_consec_seq(nums))

if __name__ == "__main__":
    main()