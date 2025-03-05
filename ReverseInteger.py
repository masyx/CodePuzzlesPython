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
        if res < int(MIN / 10) or (res == int(MIN / 10) and pop < int(math.fmod(MIN, 10))): # if x is -9463847412, returns 0
        # Neetcode version, doesn't work with numbers less than -2147483648, if x is -9463847412 returns -2147483649
        #if res < MIN // 10 or (res == MIN // 10 and pop < MIN % 10): 
            return 0
        res = (res * 10) + pop

    return res

def reverse_int_my(x: int) -> int:
    MAX_INT = 2**31 - 1
    MIN_INT = 2**31 # leaving it positive, because operating with x = abs(x) 
    
    sign = 1 if x >= 0 else -1
    res = 0
    x = abs(x)
    
    while x != 0:
        x, pop = divmod(x, 10)
        
        if sign == 1 and res > (MAX_INT - pop) // 10:
            return 0
        elif sign == -1 and res > (MIN_INT - pop) // 10:
            return 0
            
        res = res * 10 + pop
    return sign * res


def reverse_rec(x: int) -> int:
    def rec(n: int, rev: int) -> int:
        if n == 0:
            return rev
        
        if sign == -1 and rev < (1 << 31) // 10:
            return 0
        elif sign == 1 and rev > ((1 << 31) - 1) // 10:
            return 0
        
        rev = rev * 10 + n % 10
        return rec(n // 10, rev)
    
    sign = -1 if x < 0 else 1
    x = abs(x)        
    reversed_num = rec(x, 0)
    # reversed_num *= sign        
    # if reversed_num < -(1 << 31) or reversed_num > (1 << 31) - 1:
    #     return 0
        
    return reversed_num * sign

def main():
    # Solution reverse_int_my works with this number -8463847412, even though description explicitly says
    # that x is int
    
    #print(reverse_int_my(-8463847412))
    
    #print(reverse_rec(2143847412))
    print(reverse_rec(2147847412))
    

if __name__ == "__main__":
    main()