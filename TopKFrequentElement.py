'''
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
import heapq
from typing import List

# O(n) time | O(n) space
def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    counts = [[] for _ in range(len(nums) + 1)] 
    
    for num, count in freq.items():
        counts[count].append(num)
        
    res = []
    
    counts.reverse()
    for arr in counts:
        for num in arr:
            res.append(num)
            if len(res) == k:
                return res

# O(n log k) time | O(n) space, worst case where all the elements are unique, 
# dict freq will be of size n
def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq[num], num))
            elif count > heap[0][0]:
                heapq.heappushpop(heap, (freq[num], num))

        return [num for count, num in heap]
        

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
def top_k_frequent_sort(nums: List[int], k):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
    # def get_value(key):
    #     return counts[key]
    # sorted_keys = sorted(counts, key=get_value, reverse=True)
    sorted_keys = sorted(counts, key=lambda k: counts[k], reverse=True)
    return sorted_keys[0:k]


if __name__ == "__main__":
    nums = [3,0,1,0]
    k = 3
    print(top_k_frequent_sort(nums, k))
    print(top_k_frequent_heap(nums, k))