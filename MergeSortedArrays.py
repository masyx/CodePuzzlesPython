from typing import List

class Solution_Not_Space_Optimal:
    # [5,1,2,5,4]
    # [5,1,2]     [5,4]
    # [5,1] [2]   [5] [4]
    # [5] [1] recursively went down to single element in an array, start merging by comparing elements in array
    # [1,5] [2]
    # [1,2,5]     [4,5]
    # [1,2,4,5,5]
    
    

    # [5,1,2,5,4]
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        l = self.sortArray(nums[:mid])
        r = self.sortArray(nums[mid:])
        
        def mergeSort(left_arr, right_arr):
            res = []
            l_ptr = 0
            r_ptr = 0
            
            while l_ptr < len(left_arr) and r_ptr < len(right_arr):
                if left_arr[l_ptr] <= right_arr[r_ptr]:
                    res.append(left_arr[l_ptr])
                    l_ptr += 1
                else:
                    res.append(right_arr[r_ptr])
                    r_ptr += 1
                    
            while l_ptr < len(left_arr):
                res.append(left_arr[l_ptr])
                l_ptr += 1
            
            while r_ptr < len(right_arr):
                res.append(right_arr[r_ptr])
                r_ptr += 1
                
            return res
        
        return mergeSort(l, r)
    
from typing import List

class Solution_Not_Space_Optimal_Pythonic:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_arr, right_arr):
            i = j = 0
            res = []
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:   # stable tie-break
                    res.append(left_arr[i]); i += 1
                else:
                    res.append(right_arr[j]); j += 1
            res.extend(left_arr[i:])
            res.extend(right_arr[j:])
            return res

        if len(nums) <= 1:   # handles []
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return merge(left, right)
   

class Solution_Space_Optimal:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        tmp = [0] * n  # shared buffer reused for all merges

        def sort(lo: int, hi: int) -> None:
            """Sort nums[lo:hi] in place (hi is exclusive)."""
            if hi - lo <= 1:
                return

            mid = (lo + hi) // 2
            sort(lo, mid)
            sort(mid, hi)
            merge(lo, mid, hi)

        def merge(lo: int, mid: int, hi: int) -> None:
            """Merge sorted halves nums[lo:mid] and nums[mid:hi] into nums[lo:hi]."""
            i, j, k = lo, mid, lo

            while i < mid and j < hi:
                # <= makes it stable (equal elements keep original relative order)
                if nums[i] <= nums[j]:
                    tmp[k] = nums[i]
                    i += 1
                else:
                    tmp[k] = nums[j]
                    j += 1
                k += 1

            while i < mid:
                tmp[k] = nums[i]
                i += 1
                k += 1

            while j < hi:
                tmp[k] = nums[j]
                j += 1
                k += 1

            # copy merged segment back
            nums[lo:hi] = tmp[lo:hi]

        sort(0, n)
        return nums

        
if __name__ == "__main__":
    arr = [5,0,3]
    sol = Solution_Space_Optimal()
    print(sol.sortArray(arr))
    