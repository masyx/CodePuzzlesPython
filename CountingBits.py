"""338. Counting Bits
Easy

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

 

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:
0 <= n <= 105

"""

from typing import List

# O(n log n) time | O(n) space
# - Outer loop: O(n) (runs n+1 times)
# - Inner loop: O(log i) per i (runs once per set bit in i)
# Total set bits from 0 to n is O(n log n). Example: n=8 → 13 set bits.
def counting_bits_my(n: int) -> List[int]:
    result = [0] * (n + 1)
    for i in range(n + 1):
        j = i
        while j != 0:
            j &= j - 1
            result[i] += 1
    return result


"""
Example 2: n = 8
We want counts for [0, 1, 2, 3, 4, 5, 6, 7, 8].

Initialization:
    ans = [0, 0, 0, 0, 0, 0, 0, 0, 0]

x = 1:
    1 & 0 = 0
    ans[1] = ans[0] + 1 = 0 + 1 = 1
    ans = [0, 1, 0, 0, 0, 0, 0, 0, 0]

x = 2:
    2 & 1 = 0
    ans[2] = ans[0] + 1 = 0 + 1 = 1
    ans = [0, 1, 1, 0, 0, 0, 0, 0, 0]

x = 3:
    3 in binary: 11
    3 & 2 = 2 (11 & 10 = 10)
    ans[3] = ans[2] + 1 = 1 + 1 = 2
    ans = [0, 1, 1, 2, 0, 0, 0, 0, 0]

x = 4:
    4 in binary: 100
    4 & 3 = 0 (100 & 011 = 000)
    ans[4] = ans[0] + 1 = 0 + 1 = 1
    ans = [0, 1, 1, 2, 1, 0, 0, 0, 0]

x = 5:
    5 in binary: 101
    5 & 4 = 4 (101 & 100 = 100)
    ans[5] = ans[4] + 1 = 1 + 1 = 2
    ans = [0, 1, 1, 2, 1, 2, 0, 0, 0]

x = 6:
    6 in binary: 110
    6 & 5 = 4 (110 & 101 = 100)
    ans[6] = ans[4] + 1 = 1 + 1 = 2
    ans = [0, 1, 1, 2, 1, 2, 2, 0, 0]

x = 7:
    7 in binary: 111
    7 & 6 = 6 (111 & 110 = 110)
    ans[7] = ans[6] + 1 = 2 + 1 = 3
    ans = [0, 1, 1, 2, 1, 2, 2, 3, 0]

x = 8:
    8 in binary: 1000
    8 & 7 = 6 (1000 & 0111 = 0000)
    ans[8] = ans[0] + 1 = 0 + 1 = 1
    ans = [0, 1, 1, 2, 1, 2, 2, 3, 1]

Result:
    ans = [0, 1, 1, 2, 1, 2, 2, 3, 1]

Interpretation (binary → count of 1s):
    0:  0   → 0
    1:  1   → 1
    2:  10  → 1
    3:  11  → 2
    4:  100 → 1
    5:  101 → 2
    6:  110 → 2
    7:  111 → 3
    8: 1000 → 1

Why It Works:
    - x & (x - 1) removes the rightmost 1-bit from x.
    - Therefore, ans[x & (x - 1)] is the count of set bits before removing that rightmost bit.
    - Adding 1 compensates for the bit we just removed.
"""

# O(n) time | O(n) space
def counting_bits(n: int) -> List[int]:
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = result[i & (i - 1)] + 1
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
    print(counting_bits(16))