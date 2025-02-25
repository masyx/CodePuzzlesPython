from typing import List

def hamming_weight(n):
    count = 0
    while n != 0:
        n = n & (n - 1)
        count += 1
    return count

def number_set_bits(n):
    count = 0
    mask = 1
    for i in range(32):
        if (n & (mask << i)) != 0:
            count += 1
    return count

if __name__ == "__main__":
    print(bin(2147483648))
    print(hamming_weight(2147483648))
    print(number_set_bits(2147483648))
