"""853. Car Fleet
Medium

There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
You are given two integer arrays position and speed, both of length n, where position[i] is the starting
mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is
the minimum speed of any car in the fleet.
If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
Return the number of car fleets that will arrive at the destination.

 

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. 
The fleet moves at speed 1 until it reaches target.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation:
There is only one car, hence there is only one fleet.

Example 3:
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. 
The car starting at 4 (speed 1) travels to 5.
Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. 
The fleet moves at speed 1 until it reaches target.
 

Constraints:
n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106
"""



from typing import List

class Solution:
    # target = 12, 
    # idx          0 1 2 3 4
    # position = [10,8,0,5,2], 
    # speed =    [2, 4,1,1,3]
    
    # idx      0     1     2     3      4
    # arr = [(0,1),(2,3),(5,1),(8,4),(10,2)] 
    # stack = [(10,2),(5,1),(0,1)]

    # hours = (target - position) / speed
    # i = 4: hours = (12 - 10) / 2 = 1
    # i = 3: hours = (12-8) / 4 = 1
    # i = 2: hours = (12-5) / 1 = 7
    # i = 1: hours = (12-2) / 3 = 3.3 -> less time than the car if front, becomes a fleet with the car in front
    # i = 0: hours = (12-0) / 1 = 12
    
    # two cars reaching the dest together if the car in the back takes less time(or the same amount)
    # to reach the dest than the car in front 
    # can catchup: 
    # i = 3: 6,7
    # i = 4: 5,
    def car_fleet_my_first(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(position[i], speed[i]) for i in range(len(speed))]
            
        arr.sort(key=lambda car: car[0], reverse=True)
        stack = []
        
        for car in arr:
            stack.append(car)
            if len(stack) < 2: continue
            h_to_dest_curr = (target - stack[-1][0]) / stack[-1][1]
            h_to_dest_prev = (target - stack[-2][0]) / stack[-2][1]
            if h_to_dest_curr <= h_to_dest_prev:
                stack.pop()
        return len(stack)
    
    # O(n log n) time | O(n) space
    def car_fleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        
        fleets = []
        
        for pos, speed in cars:
            time_to_dest = (target - pos) / speed
            if not fleets or time_to_dest > fleets[-1]:
                fleets.append(time_to_dest)
                
        return len(fleets)
    
    
    
if __name__ == "__main__":
    target = 12
    position = [10,8,0,5,2]
    speed =    [2, 4,1,1,3]
    sol = Solution()
    print(sol.car_fleet(target, position, speed))
    print(sol.car_fleet(target, position, speed))