from typing import List


class Solution:
    # 1010
    # 1111
    #&1010
    def reverseBits(self, n: int) -> int:
        reversed_ = 0
        mask = 0x7FFFFFFF
        mask = 2 ** 31 - 1 #0x7FFFFFFF
        for i in range(31):
            bit = (n & (1 << i)) & mask
            if bit:
                reversed_ |= ((1 << (31 - i)) & mask)
        return reversed_
        
        
        
if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbao"
    
    sol = Solution()
    print(sol.reverseBits(10))