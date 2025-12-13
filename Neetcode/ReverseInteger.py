"""7. Reverse Integer
Medium
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer 
range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
 

Constraints:
-231 <= x <= 231 - 1
"""

import math

# This solution should be DISCARDED, because it makes check unnecessary for when the input 'x' is int
# Leaving it here just for the record
# Time Complexity:
    #   O(log_10(|x|)) because we process each digit of the number once.
    #   For a 32-bit integer, the maximum number of digits is constant (at most 10),
    #   so it effectively becomes O(1) in practice.
    #
    # Space Complexity:
    #   O(1) since we only use a fixed number of variables regardless of the size of x.
def reverse_int(x: int) -> int:
    MIN = -2147483648  # -2^31,
    MAX = 2147483647  #  2^31 - 1

    res = 0
    while x:
        pop = int(math.fmod(x, 10))
        x = int(x / 10)

        # the description says that x is int, so actually the input more than int is impossible
        if res > MAX // 10 or (res == MAX // 10 and pop > 7):
            return 0
        if res < int(MIN / 10) or (res == int(MIN / 10) and pop < -8): # if x is -9463847412, returns 0
            return 0
        res = (res * 10) + pop

    return res


def main():
    # Solution reverse_int_my works with this number -8463847412, even though description explicitly says
    # that x is int
    
    #print(reverse_int_my(-8463847412))
    
    #print(reverse_rec(2143847412))
    print(reverse_int(214784741))
    

if __name__ == "__main__":
    main()