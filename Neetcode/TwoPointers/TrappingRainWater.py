'''42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''


from typing import List


'''Key Concept: 
The amount of water on top of any bar is always min(leftMax, rightMax) - height[i]. 
This is central to the trapping rain water problem. It ensures that the height of water 
doesn’t exceed the smaller boundary.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]
            
            # Find the tallest bar on the left
            for j in range(i):
                leftMax = max(leftMax, height[j])
            # Find the tallest bar on the right
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])
            # Calculate trapped water at index i
            res += min(leftMax, rightMax) - height[i]
        return res
    
    
def main():
    #  5            #
    #  4        #   #
    #  3  #     #   # 
    #  2  # #   # # #
    #  1  # #   # # #
    #  0  -----------
    #     0 1 2 3 4 5
  
    height = [3,2,0,4,2,5]
    print(Solution().trap(height))
    

if __name__ == "__main__":
    main()