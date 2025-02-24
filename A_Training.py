from typing import List

def reverse_bits(n):
    result = 0
    for i in range(32):
        bit = (n >> i) & 1
        result |= bit << (31 - i)
    return result


def reverse(x: int) -> int:
    MAX_INT = 2**31 - 1 #2147483647
    MIN_INT = 2**31 #2147483648
    
    sign = 1 if x >= 0 else - 1
    x = abs(x)
    
    res = 0
    while x != 0:
        pop = x % 10
        x //= 10
        
        if res * 10 + pop > MAX_INT:
            return 0 
        
        res = res * 10 + pop

    return sign * res
    
# 1 -> 0001     # 5 -> 0101
# 2 -> 0010     # 6 -> 0110
# 3 -> 0011     # 7 -> 0111
# 4 -> 0100

# if we have n equals decimal 7(binary 0111)
# 1st iteration 7 & 6 -> 0111 & 0110 = 0110
# 2nd iteration 6 & 5 -> 0110 & 0101 = 0100
# 3rd iteration 4 & 3 -> 0100 & 0011 = 0000
if __name__ == "__main__":
    print(reverse(2147483647))
