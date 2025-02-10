"""190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. 
They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Constraints:
The input must be a binary string of length 32
"""


# O(1) time | O(1) space
def reverse_bits(n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1 # Extract the i-th bit from n
        res |= (bit << (31 - i)) # Set the corresponding bit in the reversed position
    return res

""" Step-by-Step Example
Let’s walk through a simplified example using an 8-bit number (note that LeetCode uses 32 bits, but an 8-bit example makes it easier to follow). 
Suppose we want to reverse the bits of the number n = 6. In 8-bit binary, 6 is represented as:

00000110
We want to reverse it to get:

01100000
which is equal to 96 in decimal.

Now, let’s see how the code works for each bit (using 8 iterations instead of 32 for clarity):

Initialization:

res = 0 (in binary: 00000000)

Iteration over each bit (i from 0 to 7):

Iteration 0 (i = 0):

Extract bit: (6 >> 0) & 1
6 >> 0 is still 6 → binary: 00000110
00000110 & 00000001 gives 0
Place bit: 0 << (7 - 0) → 0 << 7 = 0
Update res:
res |= 0 leaves res as 00000000

Iteration 1 (i = 1):

Extract bit: (6 >> 1) & 1
6 >> 1 is 3 → binary: 00000011
00000011 & 00000001 gives 1
Place bit: 1 << (7 - 1) → 1 << 6 = 01000000 (which is 64 in decimal)
Update res:
res |= 01000000 changes res to 01000000

Iteration 2 (i = 2):

Extract bit: (6 >> 2) & 1
6 >> 2 is 1 → binary: 00000001
00000001 & 00000001 gives 1
Place bit: 1 << (7 - 2) → 1 << 5 = 00100000 (which is 32 in decimal)
Update res:
res was 01000000 (64); OR-ing with 00100000 (32) gives 01100000 (which is 96)

Iteration 3 (i = 3):

Extract bit: (6 >> 3) & 1
6 >> 3 is 0
So the bit is 0
No change: shifting and OR-ing zero leaves res unchanged (01100000)

Iterations 4 to 7 (i = 4,5,6,7):

For these iterations, shifting 6 right by 4 or more bits results in 0
Each extracted bit is 0, so res remains 01100000

Final result:

The 8-bit reversed value is 01100000, which equals 96 in decimal.
"""


def reverse_bits_2(n: int) -> int:
    n = ((n >> 1) & 0x55555555) | ((n & 0x55555555) << 1) # Swap adjacent bits
    n = ((n >> 2) & 0x33333333) | ((n & 0x33333333) << 2) # Swap pairs of bits
    n = ((n >> 4) & 0x0F0F0F0F) | ((n & 0x0F0F0F0F) << 4) # Swap nibbles (4-bit groups)
    n = ((n >> 8) & 0x00FF00FF) | ((n & 0x00FF00FF) << 8) # Swap bytes (8-bit groups)
    n = (n >> 16) | (n << 16) # Swap 16-bit halves
    return n & 0xFFFFFFFF

# I just don't have time to understand that thoroughly 
def reverse_bits_3(self, n: int) -> int:
    res = n
    res = (res >> 16) | (res << 16) & 0xFFFFFFFF
    res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)
    res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)
    res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)
    res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)
    return res & 0xFFFFFFFF


def main():
    n = 5
    print(bin(n & 0xFFFFFFFF)[2:].zfill(32))
    print(bin(reverse_bits_2(n) & 0xFFFFFFFF)[2:].zfill(32))
    
    
if __name__ == "__main__":
    main()
