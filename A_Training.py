from typing import List

# O(n) time | O(n) space
def counting_bits(n):
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i & (i - 1)] + 1
    return res
    
if __name__ == "__main__":
    num = 10
    print(counting_bits(num))
