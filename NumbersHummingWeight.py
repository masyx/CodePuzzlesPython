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

def humming_weight_kernighans(n):
    count = 0
    while n != 0:
        n  = n & n - 1
        count += 1
    return count
    
if __name__ == "__main__":
    print(hummingWeight(10))