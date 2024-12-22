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
def counting_bits_my(n: int) -> List[int]:
    result = [0] * (n + 1)
    for i in range(n + 1):
        j = i
        while j != 0:
            j &= j - 1
            result[i] += 1
    return result

# O(n) time | O(n) space
def counting_bits(n: int) -> List[int]:
    ans = [0] * (n + 1)
    for x in range(1, n + 1):
        ans[x] = ans[x & (x - 1)] + 1
    return ans 

# 1 -> 0001     # 5 -> 0101
# 2 -> 0010     # 6 -> 0110
# 3 -> 0011     # 7 -> 0111
# 4 -> 0100

# if we have n equals decimal 7(binary 0111)
# 1st iteration 7 & 6 -> 0111 & 0110 = 0110
# 2nd iteration 6 & 5 -> 0110 & 0101 = 0100
# 3rd iteration 4 & 3 -> 0100 & 0011 = 0000


if __name__ == "__main__":
    print(counting_bits(5))