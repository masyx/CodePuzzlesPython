from collections import deque

def find_max_sliding_window(nums, w):
    deq = deque()
    for i in range(len(nums)):
        while deq and deq[0] <= i - w:
            deq.popleft()
            
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        deq.append(i)
        
        if i >= w - 1:
            result.append(nums[deq[0]])
    return result

if __name__ == "__main__":
    nums = [1,2,5,5,5,8,6]
    print(find_max_sliding_window(nums, 4))