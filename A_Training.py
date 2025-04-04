
from typing import List, Optional

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        res = max_speed
        for speed in range(min_speed, max_speed + 1):
            hours = 0
            for i, pile in enumerate(piles):
                while pile > 0 and hours < h:
                    pile -= speed
                    hours += 1
                if i == len(piles) - 1 and pile <= 0:
                        res = min(speed, res)
        return res
        
    
    
def main():
    piles = [30,11,23,4,20]
    h = 5
    solution = Solution()
    print(solution.minEatingSpeed(piles, h))
    
     
if __name__ == "__main__":
    main()
        