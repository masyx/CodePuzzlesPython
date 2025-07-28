import math
from typing import List, Optional
from collections import deque

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        
        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            hours_to_finish = 0
            for pile in piles:
                hours_to_finish += math.ceil(pile / mid_speed)

            if hours_to_finish > h:
                min_speed = mid_speed + 1
            else:
                max_speed = mid_speed - 1
        return min_speed
        
# n = 3       
def main():
    piles = [3,6,7,11]
    h = 8
    sol = Solution()
    print(sol.minEatingSpeed(piles, h))



    
    
if __name__ == "__main__":
    main()
        