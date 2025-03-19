'''11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

 

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
 

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

from typing import List

# i is width
# [1,8,6,2,5,4,8,3,7]
def max_area_bf(heights: List[int])-> int:
    res = 0
    for l in range(len(heights)- 1):
        for r in range(l + 1, len(heights)):
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
    return res

def max_area(heights: List[int]) -> int:
    res = 0
    l = 0
    r = len(heights) - 1
    while l < r:
        curr_area = (r - l) * min(heights[l], heights[r])
        res = max(res, curr_area)
        
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res


def main():
    heights = [3,2,4,5,1]
    print(max_area_bf(heights))
    print(max_area(heights))
    
    
if __name__ == "__main__":
    main()