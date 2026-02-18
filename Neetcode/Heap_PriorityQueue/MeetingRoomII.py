'''253. Meeting Rooms II
Medium

Given an array of meeting time intervals intervals where intervals[i] = [start ith, end ith], 
return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
 
Constraints:
1 <= intervals.length <= 104
0 <= start < end <= 106
'''

from typing import List
import heapq

class Solution:
    # intervals = [[0,30],[5,10],[15,20]]
    # Sort by start time; a meeting can only reuse a room whose prior meeting already ended.
    # Keep a min-heap of end times for rooms currently in use (heap size = rooms in use; heap[0] ends earliest).
    # For each (s, e): if heap and s >= heap[0], pop to reuse that room; push e either way.
    # If s < heap[0], no room is free yet → need a new room. Track max heap size = minimum rooms required.

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        heap = []
        
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
            
        return len(heap)
    
    
if __name__ == "__main__":
    meetings = [(0,40),(5,10),(5,10),(15,30),(20,35)] # 3 rooms
    sol = Solution()
    print(sol.minMeetingRooms(meetings))