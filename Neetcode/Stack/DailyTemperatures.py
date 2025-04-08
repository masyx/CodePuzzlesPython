""" 739. Daily Temperatures
Medium
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. If there is no future day for which
this is possible, keep answer[i] == 0 instead.

 
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

from typing import List
class Solution:
    #                      v
    #i      0  1  2  3  4  5  6  7
    #     [73,73,72,71,69,72,76,73]
    #ans  [ 0, 0, 0, 0, 0, 0, 0, 0]
    #stack[0,1,2,3,4,5]
    
    
    # When I see repeating statement 'stack.append(i - 1)' it means that there is definitely a room for optimization
    # Here I have if-else statement but in both cases I append to the stack, which means if-else
    # can be removed. 
    def daily_temperatures_my(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i in range(1, len(temperatures)):
            curr_temp = temperatures[i]
            prev_temp = temperatures[i - 1]
            if curr_temp <= prev_temp:
                stack.append(i - 1)
            else:
                stack.append(i - 1)
                while stack and temperatures[stack[-1]] < curr_temp:
                    lower_temp_day_idx = stack.pop()
                    answer[lower_temp_day_idx] = i - lower_temp_day_idx
        return answer
    
    
    #       V
    #i      0  1  2  3  4  5  6  7
    #     [73,73,72,71,69,72,76,73]
    #ans  [ 6, 5, 4, 2, 1, 1, 0, 0]
    #stack[ 6, 7 ]
    def daily_temperatures_my_optimized(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        prev_days = []
        for curr_day in range(1, len(temperatures)):
            curr_temp = temperatures[curr_day]
            prev_days.append(curr_day - 1)
            while prev_days and curr_temp > temperatures[prev_days[-1]]:
                prev_day = prev_days.pop()
                answer[prev_day] = curr_day - prev_day
        return answer
    
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        prev_days = []
        for curr_day in range(len(temperatures)):
            curr_temp = temperatures[curr_day]
            
            while prev_days and curr_temp > temperatures[prev_days[-1]]:
                prev_day = prev_days.pop()
                answer[prev_day] = curr_day - prev_day
            
            prev_days.append(curr_day)
        return answer


def main():
    temps = [73,73,72,71,69,72,76,73]

    solution = Solution()
    print(solution.daily_temperatures_my(temps))
    print(solution.daily_temperatures_my_optimized(temps))
    print(solution.daily_temperatures(temps))
    
    
     
if __name__ == "__main__":
    main()