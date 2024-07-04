from collections import deque

def max_sliding_window(nums, w):
    if not nums:
        return []

    deq = deque()
    result = []

    for i in range(len(nums)):
        # Remove indices that are out of the current window
        if deq and deq[0] <= i - w:
            deq.popleft()

        # Remove elements from deque that are smaller than the current element
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        # Add the current element's index to the deque
        deq.append(i)

        # If the window is fully within the list, add the maximum to the result
        if i >= w - 1:
            result.append(nums[deq[0]])

    return result


if __name__ == "__main__":
    nums = [0, 0, 9, 0, 8, 3]
    w = 2
    print(max_sliding_window(nums, w))