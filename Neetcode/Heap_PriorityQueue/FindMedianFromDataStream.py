"""295. Find Median from Data Stream

Hard

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:
-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""


class MedianFinderBF:
    #      0 1 2
    #arr: [2 3 4]
    # if len(nums) is odd then we return nums[len(nums) // 2] else: (nums[len(nums) // 2] + nums(len(nums)//2 + 1)) / 2
    def __init__(self):
        self.nums = []
        self.median = 0        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()
        
        n = len(self.nums)
        if n % 2 != 0: # odd number
            self.median = self.nums[n // 2]
        else:
            self.median = (self.nums[n // 2] + self.nums[(n // 2) -1]) / 2


    def findMedian(self) -> float:
        return self.median

import heapq

#                <- ->
# final state representation: [0 3 5 6 8 12]
# arr: [0 3 5 6]
# max_heap: [-3, 0]
# min_heap: [5 6]
# count: 3 4
#
# called FindMedian: 5
class MedianFinder:
    def __init__(self):
        # max_heap stores the lower half as negatives so we can use heapq (min-heap)
        self.max_heap = []  # contains negatives: largest element of lower half is -self.max_heap[0]
        # min_heap stores the upper half as normal min-heap
        self.min_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        """
        Add a number into the data structure.
        Strategy:
          - If max_heap is empty or num <= -max_heap[0] (i.e., ≤ max of lower half) -> push into max_heap.
          - Otherwise push into min_heap.
          - Rebalance sizes so that len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1.
        """
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Rebalance: ensure max_heap has either same size as min_heap or one more element.
        if len(self.max_heap) > len(self.min_heap) + 1:
            # move top from max_heap to min_heap
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            # move top from min_heap to max_heap
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

        self.count += 1

    def findMedian(self) -> float:
        """
        Return median:
          - if odd total count -> top of max_heap
          - if even -> average of tops of max_heap and min_heap
        """
        if self.count == 0:
            raise ValueError("No elements yet")

        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            # even number of elements
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0



if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # 1.5
    mf.addNum(3)
    print(mf.findMedian())  # 2.0

    # more testing
    seq = [5,2,10,3]
    mf2 = MedianFinder()
    for x in seq:
        mf2.addNum(x)
        print("added", x, "median now", mf2.findMedian())
    