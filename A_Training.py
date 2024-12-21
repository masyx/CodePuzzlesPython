from typing import List

# O(32) -> O(1) time | O(1) space
def hammingWeight(n):
    count = 0
    mask = 1 # ... 0001
    for _ in range(32):
        if (n & mask) != 0:
            count += 1
        mask <<= 1
    return count

# n & (n - 1)
def hamming_weight(n: int):
    count = 0
    while n != 0:
        n &= (n - 1)
        count += 1
    return count


def singleNumber(nums: List[int]):
    result = 0
    for num in nums:
        result ^= num
    return result
    
# 1 -> 0001     # 5 -> 0101
# 2 -> 0010     # 6 -> 0110
# 3 -> 0011     # 7 -> 0111
# 4 -> 0100

# if we have n equals decimal 7(binary 0111)
# 1st iteration 7 & 6 -> 0111 & 0110 = 0110
# 2nd iteration 6 & 5 -> 0110 & 0101 = 0100
# 3rd iteration 4 & 3 -> 0100 & 0011 = 0000
if __name__ == "__main__":
    print(singleNumber([2,2,99,5,5]))
