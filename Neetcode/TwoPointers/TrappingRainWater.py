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
    def trap_bf(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        
        for i in range(1, len(height)):
            left_max = right_max = height[i]
            
            for j in range(i):
                left_max = max(left_max, height[j])
            for j in range(i + 1, len(height)):
                right_max = max(right_max, height[j])
                
            res += min(left_max, right_max) - height[i]
        return res

    """Drawings
        
             i:     0 1 2 3 5 6
        height:    [3,2,0,5,2,4]
        left_max:  [3,3,3,5,5,5]
        right_max: [5,5,5,5,4,4]
        
    """
    def trap_dp(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n
        
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res

    """Key Point
    The key insight is that the amount of water trapped at any position is limited by the smaller of the two maxima (left and right).
    By always moving the pointer on the side with the smaller maximum, we can be sure that the water at the new position is determined 
    by that smaller maximum, because the other side’s maximum is at least as tall. This lets us calculate the water on the fly without 
    needing to know the exact maximum on the opposite side for every position—we just need to know it’s bigger.
    
    Start with the goal: for each bar, we need min(max_left, max_right) - height[i]
    
    Key Decision: Compare leftMax and rightMax. If leftMax is smaller, the water at the next left position can’t exceed leftMax, 
    no matter how tall the right side is (since it’s at least rightMax). So, we can safely move left and compute water based on leftMax. 
    If rightMax is smaller or equal, the same applies on the right.
    
    This reasoning leads to the comparison if leftMax < rightMax: it’s about identifying which side’s maximum is the limiting factor right
    now and processing that side, trusting that the other side’s height will hold the water.
    
    
    By always stepping forward from the side with the shorter maximum wall, you can figure out how much water sits at each spot as you go, 
    because the taller wall on the other side ensures the water won’t spill over there. 
    """
    def trap_two_pointers(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
            
            
def main():
    #  5        #    
    #  4        #   
    #  3  #     #    
    #  2  # #   # # #
    #  1  # #   # # #
    #  0  -----------
    #     0 1 2 3 4 5
  
    height = [3,2,0,5,2,2]
    #height = [1,3,5,4]
    print(Solution().trap_bf(height))
    print(Solution().trap_dp(height))
    print(Solution().trap_two_pointers(height))


    

if __name__ == "__main__":
    main()