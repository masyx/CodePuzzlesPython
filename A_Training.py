from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List

class Solution:
    # nums = [1,2,2,3,3], k = 2
    # freq: 1-1, 2-2, 3-2
    # i          
    # buckets: [
        #0[]
        #1[1]
        #2[2,3]
        #3[]
        #4[]
        #5[]
        #6[]]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)] # if all numbers is the same number
        
        for num, count in freq.items():
            buckets[count].append(num)
        
        res = []
        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res

if __name__ == "__main__":

    nums = [1,2,2,3,3]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k))