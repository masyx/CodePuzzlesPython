from typing import List

# O(n) time | O(n + m) space
def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
    num3 = [0] * (len(num1) + len(num2))
    i, j, k = 0, 0, 0,
    while i != len(num1) or j != len(num2):
        if j == len(num2) or (i < len(num1) and num1[i] < num2[j]):
            num3[k] = num1[i]
            i += 1
        else:
            num3[k] = num2[j]
            j += 1
        k += 1
    mid_idx = (len(num3) - 1) // 2
    if len(num3) & 1 == 1:
        return num3[mid_idx]
    else:
        return (num3[mid_idx] + num3[mid_idx + 1]) / 2.0
    
# The function findMedianOfTwoArrays takes two input arrays num1 and num2, 
# both of type List. The input arrays contain integers. The function returns a list 
# of integers representing the median of the two arrays.
# The function starts by creating a new array num3 of length equal to the sum of the lengths
# of num1 and num2. The variable i is used to iterate over num1, j is used to iterate over num2,
# and k is used to fill num3 with elements from num1 and num2.
# The while loop continues until either i reaches the end of num1 or j reaches the end of num2. 
# In each iteration, the code checks if j has reached the end of num2 or if the current element 
# in num1 is less than the current element in num2 (and i is still within the bounds of num1). 
# If the first condition is true, the element from num1 is added to num3. If the second 
# condition is true, the element from num2 is added to num3. 
# In both cases, k is incremented to move to the next position in num3.
# Once the while loop has completed, the median of num3 is calculated 
# by finding the middle index (mid_idx). If the length of num3 is odd, the function returns 
# the element at the mid_idx. If the length of num3 is even, the function returns 
# the average of the elements at mid_idx and mid_idx + 1.

# O(n) time | O(n + m) space
def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
    num3 = [0] * (len(num1) + len(num2))
    i, j, k = 0, 0, 0
    while i != len(num1) or j != len(num2):
        if j == len(num2) or (i < len(num1) and num1[i] < num2[j]):
            num3[k] = num1[i]
            i += 1
        else:
            num3[k] = num2[j]
            j += 1
        k += 1
    med_idx = (len(num3) - 1) // 2
    if len(num3) % 2 == 0:
        return (num3[med_idx] + num3[med_idx + 1]) / 2.0
    else:
        return num3[med_idx]

def main():
    l1 = [1]
    l2 = [2,3,4]
    print(findMedianSortedArrays(l1, l2))
    
    
if __name__ == "__main__":
    main()