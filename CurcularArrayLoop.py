import random
import time

"""
Statement:
We are given a circular array of non-zero integers, nums, where each integer represents 
the number of steps to be taken either forward or backward from its current index. 
Positive values indicate forward movement, while negative values imply backward movement. 
When reaching either end of the array, the traversal wraps around to the opposite end.

The input array may contain a cycle, which is a sequence of indexes characterized by the following:
1. The sequence starts and ends at the same index.
2. The length of the sequence is at least two.
3. The loop must be in a single direction, forward or backward.

Note: A cycle in the array does not have to originate at the beginning. It may begin from any point in the array.

Your task is to determine if nums has a cycle. Return True if there is a cycle. Otherwise, return False.

Constraints:
1 <= nums.length <= 10^3
-5000 <= nums[i] <= 5000
nums[i] != 0
"""

# Example of an Array with a Loop
array_with_loop = [2, -1, 1, 2, 2]
# Explanation:
# - Start at index 0: move 2 steps to index 2
# - From index 2: move 1 step to index 3
# - From index 3: move 2 steps to index 0
# The sequence is 0 → 2 → 3 → 0, forming a loop.

# Example of an Array without a Loop
array_without_loop = [1, 2, -1, 2]
# Explanation:
# - Start at index 0: move 1 step to index 1
# - From index 1: move 2 steps to index 3
# - From index 3: move 2 steps to index 1
# - From index 1: move 2 steps to index 3
# The sequence repeats between indexes 1 and 3, but it does not form a valid cycle.
# The criteria for a cycle require that the sequence must return to the starting index in a single continuous direction.


def circular_array_loop(nums):
    return random.choice([True, False])


if __name__ == "__main__":
    print(f"Does array {array_with_loop} has a loop? - {'Yes' if circular_array_loop(array_with_loop) else 'No'}")
    print(f"Does array {array_without_loop} has a loop? - {'Yes' if circular_array_loop(array_without_loop) else 'No'}")


