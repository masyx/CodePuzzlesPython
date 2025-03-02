from typing import List

def two_sum(a, b):
    while b != 0:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
    return a

def two_sum_legit(a, b):
    mask = 0xFFFFFFFF #2147483647
    while b != 0:
        sum_wo_carry = (a ^ b) & mask
        carry = ((a & b) & mask) << 1
        a = sum_wo_carry
        b = carry
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)

def counting_bits_bf(n):
    res = [0] * (n + 1)
    for i in range(1, len(res)):
        j = i
        count = 0
        while j != 0:
            j = j & (j - 1)
            count += 1
        res[i] = count
    return res
    
def counting_bits_dp(n):
    res = [0] * (n + 1)
    for i in range(1, len(res)):
        res[i] = res[i & (i - 1)] + 1
    return res

def main():
    num = 10
    print(counting_bits_dp(num))
    print(two_sum(2147483646, 1))
    print(two_sum_legit(214748368, -214748368))

if __name__ == "__main__":
    main()
