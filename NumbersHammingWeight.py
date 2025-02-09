"""191. Number of 1 Bits
Easy
Given a positive integer n, write a function that returns the number of 
set bits in its binary representation (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation: The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation: The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation: The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
1 <= n <= 231 - 1

"""

#O(32) -> O(1) time | O(1) space
def hummingWeight(n):
    count = 0
    mask = 1
    for _ in range(32):
        if (n & mask) != 0:
            count += 1
        mask <<= 1
    return count

# O(k) where k is the number of set bits -> O(1) | O(1) space
def humming_weight_kernighans(n):
    count = 0
    while n != 0:
        n  &= n - 1 # every iteration removes the least significant bit
        count += 1
    return count

""" Example of Kernighans algorithm
 This effectively reduces the number of 1s in n by 1 with each operation. The algorithm stops when 
 n becomes 0, and the number of operations is equal to the number of 1s in n.
 1 -> 0001     # 5 -> 0101
 2 -> 0010     # 6 -> 0110
 3 -> 0011     # 7 -> 0111
 4 -> 0100
 
 if we have n equals decimal 7(binary 0111)
 1st iteration 7 & 6 -> 0111 & 0110 = 0110
 2nd iteration 6 & 5 -> 0110 & 0101 = 0100
 3rd iteration 4 & 3 -> 0100 & 0011 = 0000"""

if __name__ == "__main__":
    print(hummingWeight(10))