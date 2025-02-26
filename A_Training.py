from typing import List

# 0b0000 0101
# 0b1010 0000
# 128+32 = 160
# O(1) time | O(1) space
def reverse_bits(n):
    res = 0
    for i in range(32):
        bit = n & 1
        res = res | (bit << (31 - i))
        n >>= 1
    return res

def reverseBits(n: int) -> int:
    res = n
    res = (res >> 16) | (res << 16) & 0xFFFFFFFF
    res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)
    res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)
    res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)
    res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)
    return res & 0xFFFFFFFF
    
    
if __name__ == "__main__":
    n = 1 #2147483648
    print(bin(n))
    print(reverse_bits(n))
