
from typing import List, Optional
import math

class Solution:
    # O(nm) time, where n is speed and m is number of piles | O(1) space
    def minEatingSpeed_bf(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            hours_spent = 0
            
            for pile in piles:
                hours_spent += math.ceil(pile / speed)
                
            if hours_spent > h:
                speed += 1
            else:
                return speed
                
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed, max_speed = 0, max(piles)
        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile / mid_speed)
            
            if hours_spent > h:
                min_speed = mid_speed + 1
            else:
                max_speed = mid_speed - 1
        return min_speed
        
    
    
def main():
    piles = [30,11,23,4,20]
    h = 6
    solution = Solution()
    print(solution.minEatingSpeed_bf(piles, h))
    print(solution.minEatingSpeed(piles, h))
    
     
if __name__ == "__main__":
    main()
        