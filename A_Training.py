from typing import List

def reverse_bits(n):
    result = 0
    for i in range(32):
        bit = (n >> i) & 1
        result |= bit << (31 - i)
    return result


def reverse(x: int) -> int:
    # Define the 32-bit signed integer boundaries.
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648

    result = 0
    # Record the sign and work with the absolute value.
    sign = 1 if x >= 0 else -1
    x = abs(x)
    
    while x != 0:
        # Pop the last digit from x.
        pop = x % 10
        x //= 10
        
        # Before pushing the digit into result,
        # check for potential overflow.
        if result > (INT_MAX - pop) // 10:
            return 0
        
        # Multiply result by 10 using bit manipulation.
        # Multiplying by 10 = result*8 + result*2, which is:
        result = (result << 3) + (result << 1) + pop
        
    return sign * result
    

# 1 -> 0001     # 5 -> 0101
# 2 -> 0010     # 6 -> 0110
# 3 -> 0011     # 7 -> 0111
# 4 -> 0100

# if we have n equals decimal 7(binary 0111)
# 1st iteration 7 & 6 -> 0111 & 0110 = 0110
# 2nd iteration 6 & 5 -> 0110 & 0101 = 0100
# 3rd iteration 4 & 3 -> 0100 & 0011 = 0000
if __name__ == "__main__":
    print(bin(reverse_bits(5)))
