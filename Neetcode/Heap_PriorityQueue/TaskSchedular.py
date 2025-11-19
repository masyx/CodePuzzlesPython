""" 621. Task Scheduler
Medium

You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU 
interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's
a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

 

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two intervals before doing A again. The same applies to task B. 
In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. 
This leads to idling twice between repetitions of these tasks.

 

Constraints:
1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100

"""


from collections import deque
import heapq
from typing import Counter, List

class Solution:
    # tasks = ["A","A","A","B","B"], n = 2; res = 7
    #              123456789
    # ba_ba__a 8;  ab_ab_a 7
    # cooldown: curr_time + n + 1

    # heap: [  ]
    # cnt = -2 + 1 = -1
    # queue: [(-2, 3), (-1, 4)]
    # time 3: -3 will be available at: 1 + 2 + 1 = 4
    def leastInterval_no_jump(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        
        time = 0
        q = deque()
        
        while max_heap or q:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt:
                    q.append((cnt, time + n)) # (task_count, time_avail)

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        
        time = 0
        q = deque()
        
        while max_heap or q:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt:
                    q.append((cnt, time + n)) # (task_count, time_avail)
            else:
                time = q[0][1] # jump clock to the time when the first task in the cooldown queue is available

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
    
    
    
if __name__ == "__main__":
    tasks = ["A","C","A","B","D","B"]
    n = 1
    sol = Solution()
    print(sol.leastInterval_no_jump(tasks, n))
    print(sol.leastInterval(tasks, n))
            