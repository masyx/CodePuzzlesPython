""" 346. Moving Average from Data Stream

Easy

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
Implement the MovingAverage class:
MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
 

Example 1:
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 

Constraints:
1 <= size <= 1000
-105 <= val <= 105
At most 104 calls will be made to next.
"""


from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.nums = deque()
        

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.sum += val 
        if len(self.nums) > self.size:
            self.sum -= self.nums.popleft()
        return self.sum / len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


class MovingAverage2:
    def __init__(self, size: int):
        self.size = size
        self.buffer = [0] * size   # fixed-size circular buffer
        self.idx = 0               # next position to write
        self.count = 0             # how many elements we've stored (<= size)
        self.window_sum = 0.0      # running sum of current window

    def next(self, val: int) -> float:
        if self.count < self.size:
            # Still filling the buffer; no eviction yet
            self.count += 1
            self.window_sum += val
            self.buffer[self.idx] = val
        else:
            # Buffer full: evict the oldest value at idx, insert new one
            old = self.buffer[self.idx]
            self.window_sum += val - old
            self.buffer[self.idx] = val

        # Move index forward in circular fashion
        self.idx = (self.idx + 1) % self.size

        return self.window_sum / self.count


if __name__ == "__main__":
    # Example from the problem statement
    movingAverage = MovingAverage(3)
    print(movingAverage.next(1))   # 1.0  = 1 / 1
    print(movingAverage.next(10))  # 5.5  = (1 + 10) / 2
    print(movingAverage.next(3))   # 4.666666666666667 = (1 + 10 + 3) / 3
    print(movingAverage.next(5))   # 6.0  = (10 + 3 + 5) / 3
    print()
    
    movingAverage2 = MovingAverage2(3)
    print(movingAverage2.next(1))   # 1.0  = 1 / 1
    print(movingAverage2.next(10))  # 5.5  = (1 + 10) / 2
    print(movingAverage2.next(3))   # 4.666666666666667 = (1 + 10 + 3) / 3
    print(movingAverage2.next(5))   # 6.0  = (10 + 3 + 5) / 3






