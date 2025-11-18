"""


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

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
            