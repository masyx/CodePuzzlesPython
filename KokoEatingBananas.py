'''
875. Koko Eating Bananas
Medium

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of curr_speed. Each hour, she chooses some pile of bananas 
and eats curr_speed bananas from that pile. If the pile has less than curr_speed bananas, she eats all of them 
instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer curr_speed such that she can eat all the bananas within h hours.

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


def min_eating_bananas(piles: List[int], h: int):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        curr_speed = (l + r) // 2

        totalTime = 0
        for p in piles:
            totalTime += math.ceil(float(p) / curr_speed)
        if totalTime <= h:
            res = curr_speed
            r = curr_speed - 1
        else:
            l = curr_speed + 1
    return res


if __name__ == "__main__":
    piles = [312884470]
    print(min_eating_bananas(piles, 312884469))