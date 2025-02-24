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

        if res > MAX // 10 or (res == MAX // 10 and pop > MAX % 10):
            return 0
        if res < MIN // 10 or (res == MIN // 10 and pop < MIN % 10):
            return 0
        res = (res * 10) + pop

    return res

def reverse_int_my(x: int) -> int:
    MAX_INT = 2**31 - 1
    
    sing = 1 if x >= 0 else -1
    res = 0
    x = abs(x)
    
    while x != 0:
        pop = x % 10
        x = x // 10
        x, pop = divmod(x, 10)
        
        if res > (MAX_INT - pop) // 10:
            return 0
        
        res = res * 10 + pop
    
    return sing * res


def main():
    print(reverse_int_my(-1563847412))
    

if __name__ == "__main__":
    main()