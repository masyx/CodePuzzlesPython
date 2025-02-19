
# Time Complexity:
    #   O(log_10(|x|)) because we process each digit of the number once.
    #   For a 32-bit integer, the maximum number of digits is constant (at most 10),
    #   so it effectively becomes O(1) in practice.
    #
    # Space Complexity:
    #   O(1) since we only use a fixed number of variables regardless of the size of x.
def reverse_int(x):
    # Define the 32-bit singed int boundaries
    INT_MAX = 2**31 - 1 # 2147483647
    INT_MIN = 2**31     # 2147483648
    
    result = 0
    # Record the sing and work with the absolute value
    sign = 1 if x >= 0 else -1
    x = abs(x)
    
    while x != 0:
        # Pop the last digit from x
        pop = x % 10
        x //= 10
        
        if result > (INT_MAX - pop) // 10:
            return 0
        
        result = result * 10 + pop
        # 10 = result*8 + result*2
        #result = (result << 3) + (result << 1) + pop
    
    return sign * result


def main():
    print(reverse_int(-2147483642))
    

if __name__ == "__main__":
    main()