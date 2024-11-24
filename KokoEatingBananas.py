'''
875. Koko Eating Bananas
Medium

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas 
and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them 
instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:

1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
'''

import math
from typing import List


#i 0  1  2   3
# [5, 3, 1, 4] h = 4
# speed min = 5, max = 5, medium = 4 
# result = 5

def min_eating_speed(piles: List[int], h):
    min_speed, max_speed = 1, max(piles)
    result = max_speed
    while min_speed <= max_speed:
        medium_speed = (max_speed + min_speed) // 2
        hours_spent = 0
        for pile in piles:
            hours_spent += math.ceil(pile / medium_speed)
        if hours_spent > h:
            min_speed = medium_speed + 1
        else:
            max_speed = medium_speed - 1
    return min_eating_speed


if __name__ == "__main__":
    piles = [30,11,23,4,20]
    h = 6
    
    print(min_eating_speed(piles, h))