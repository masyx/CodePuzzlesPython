"""
We are given an points list containing datapoints for a metric that we receive from our customers, 
and we want to apply a smoothing function (a moving sum) when they are displayed. 
points_points = [ 
{"tags": ["env:dev"], "timestamp": 0, "value": 1}, 
{"tags": ["env:dev"], "timestamp": 1, "value": 3}, 
{"tags": ["env:prod","host:a"], "timestamp": 2, "value": 5}, 
{"tags": ["env:dev"], "timestamp": 3, "value": -1}, 
{"tags": ["env:dev","host:a"], "timestamp": 6, "value": -3},
{"tags": ["env:dev"], "timestamp": 7, "value": 5}, 
{"tags": ["env:staging","host:a"], "timestamp": 9, "value": -3}, 
{"tags": ["env:dev"], "timestamp": 10, "value": -4}, 
{"tags": ["env:dev"], "timestamp": 11, "value": 6}, 
{"tags": ["env:dev"], "timestamp": 14, "value": -1}, 
{"tags": ["env:staging"], "timestamp": 15, "value": 10} ] 

Write a smoothing function that works like this: for all points associated with tag t, 
calculate the sum of each consecutive window of k points. We plan to run our smoothing function many times, 
with different values of t and k, on the same dataset. 
A point is associated with tag t if the tag is included along with the point. 
So the list of points associated with the tag env:dev, as tuples of (timestamp, value) 
is [(0, 1), (1, 3), (3, -1), (6, -3), (7, 5), (10, -4), (11, 6), (14, -1)]. 
The sliding windows of size 3 moving across these points are then: 
[  (0,1), (1,3), (3,-1), (6,-3), (7,5), (10,-4), (11,6), (14,-1)] 
[ [(0,1), (1,3), (3,-1), (6,-3), (7,5), (10,-4), (11,6), (14,-1)] 
# [(0,1), (1,3), (3,-1), (6,-3), (7,5), (10,-4), (11,6), (14,-1)] 
# [(0,1), (1,3), (3,-1), (6,-3), (7,5), (10,-4), (11,6), (14,-1)] 
# [(0,1), (1,3), (3,-1), (6,-3), (7,5), (10,-4), (11,6), (14,-1)] ]
"""


from collections import deque
from typing import List, Dict, Any
class Solution:

    def smooth(self, points, tag, k):
        res = []
        filtered = deque()
        for point in points:
            if tag in point["tags"]:
                filtered.append(point["value"])
                if len(filtered) == k:
                    res.append(sum(filtered))
                    filtered.popleft()
        return res
    #  0 1 2 3 4 5
    #  1 2 3 4 5 6

    def smooth(self, points: List[Dict[str, Any]], tag: str, k: int) -> List[int]:
        if k <= 0:
            return []

        # If input is not guaranteed sorted by timestamp, uncomment:
        # points = sorted(points, key=lambda p: p["timestamp"])

        res: List[int] = []
        window = deque()
        window_sum = 0

        for point in points:
            if tag in point["tags"]:
                value = point["value"]
                window.append(value)
                window_sum += value

                if len(window) == k:
                    res.append(window_sum)
                    window_sum -= window.popleft()

        return res
    



                    
    
def main():
    points_points = [
        {"tags": ["env:dev"], "timestamp": 0, "value": 1}, 
        {"tags": ["env:dev"], "timestamp": 1, "value": 3}, 
        {"tags": ["env:prod","host:a"], "timestamp": 2, "value": 5}, 
        {"tags": ["env:dev"], "timestamp": 3, "value": -1}, 
        {"tags": ["env:dev","host:a"], "timestamp": 6, "value": -3},
        {"tags": ["env:dev"], "timestamp": 7, "value": 5}, 
        {"tags": ["env:staging","host:a"], "timestamp": 9, "value": -3}, 
        {"tags": ["env:dev"], "timestamp": 10, "value": -4}, 
        {"tags": ["env:dev"], "timestamp": 11, "value": 6}, 
        {"tags": ["env:dev"], "timestamp": 14, "value": -1}, 
        {"tags": ["env:staging"], "timestamp": 15, "value": 10} ]
    
    sol = Solution()
    print(sol.smooth(points_points, "env:dev", 3))
    print(sol.smooth_improved(points_points, "env:dev", 3))
  
  
if __name__ == "__main__":
    main()