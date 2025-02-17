"""371. Sum of Two Integers
Medium

Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:
Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:
-1000 <= a, b <= 1000
"""


"""=======  C# Solution =========

public class Solution {
    // public int GetSum(int a, int b) {
    //     while(b != 0){
    //         var answer = a ^ b;
    //         var carry = a & b;
    //         a = answer;
    //         b = carry << 1;
    //     }
    //     return a;
    // }

    public int GetSum(int a, int b) {
        while(b != 0){
            var carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
}

"""

# O(1) time | O(1) space
def get_sum(a: int, b: int) -> int:
    # Define a 32-bit mask: 0xFFFFFFFF has all 32 bits set to 1.
    # This mask ensures that after each operation, we keep only the lower 32 bits.
    mask = 0xFFFFFFFF
    
    # Continue looping until there is no carry (b becomes 0).
    while b != 0:
        # Compute the sum without carry:
        # a ^ b adds the bits where there is no carry.
        # Applying & mask here discards any bits beyond the 32nd bit.
        sum_without_carry = (a ^ b) & mask

        # Compute the carry:
        # a & b finds all the bits where both a and b have 1's (i.e., where a carry is generated).
        # (a & b) << 1 shifts these carry bits to their proper positions.
        # Again, applying & mask ensures that if the left shift produced extra bits, they are discarded.
        carry = ((a & b) << 1) & mask
        
        # Update a and b for the next iteration:
        a, b = sum_without_carry, carry
    
    # After the loop, 'a' holds the result in a simulated 32-bit integer.
    # In a 32-bit system, the maximum positive integer is 0x7FFFFFFF.
    max_int = 0x7FFFFFFF
    
    # If 'a' is within the 32-bit positive range, return it as is.
    # Otherwise, convert the 32-bit two's complement negative number to a proper Python negative integer.
    return a if a <= max_int else ~(a ^ mask)


def main():
    print(get_sum(99, 1))
    
    
if __name__ == "__main__":
    main()
