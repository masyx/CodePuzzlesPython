from collections import deque

def maxSlidingWindow(nums, w):
    deq = deque()
    result = []
    for i in range(len(nums)):
        # remove indices that are out of the current window
        while deq and deq[0] <= i - w:
            deq.popleft()
            
        # remove elements that are smaller than the current value
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        # add the current element's index to the deq
        deq.append(i)
        
        # If the window is completely withing the list add the biggest value to the result
        if i >= w - 1:
            result.append(nums[deq[0]])
    return result
if __name__ == "__main__":
    arr = [2,4,1,5,8]
    print(maxSlidingWindow(arr, 3))