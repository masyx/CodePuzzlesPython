from typing import List

'''Time/Space complexity
Time Complexity Analysis:
Constructing the frequency dictionary: O(n)
Sorting the unique keys: O(u log u)
Slicing the first k elements: O(k) (negligible in big-O notation)
Overall: O(n + u log u)
Since u (unique elements) is at most n (worst case: all elements unique),
this simplifies to O(n log n) in the worst case.

Space Complexity Analysis:
Dictionary `counts`: O(u)
Sorted list `sorted_keys`: O(u)
Output list: O(k)
Overall: O(u + k)
Since u ≤ n, this simplifies to O(n + k) in the worst case.
'''
def top_k_frequent(nums: List[int], k):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
    # def get_value(key):
    #     return counts[key]
    # sorted_keys = sorted(counts, key=get_value, reverse=True)
    sorted_keys = sorted(counts, key=lambda k: counts[k], reverse=True)
    return sorted_keys[0:k]


def main():
    arr = [2,2,5,5,5,3,3,3,3,1,1,1,1,1,1,1,1,1,1]
    print(top_k_frequent(arr, 3))
    
if __name__ == "__main__":
    main()