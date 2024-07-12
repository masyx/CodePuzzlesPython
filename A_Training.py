from collections import deque
def maxSlidingWindow(nums, w):
    result = []
    deq = deque()
    for i in range(len(nums)):
        # Remove indices that are out of the current window limits
        while deq and deq[0] < i + 1 - w:
            deq.popleft()
        
        # Remove indices of the elements that are less than the 
        # current element
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        # Append the current element's index to the deque
        deq.append(i)
        
        # Start adding the maximum value to the result array one the first window is fully 
        # withing the list
        if i >= w - 1:
            result.append(nums[deq[0]])
    return result
    
    
if __name__ == "__main__":
    nums = [11, 3, 50, 0]
    print(maxSlidingWindow(nums, 2))
    