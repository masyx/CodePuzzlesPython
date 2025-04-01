from typing import List

def generate_binary(n, current=""):
    if len(current) == n:
        print(current)
        return 1 # One valid combination found

    # Count from left and right branches
    count = 0 
    # Try '0'
    count += generate_binary(n, current + "0")
    # Backtrack and try '1'
    count += generate_binary(n, current + "1")
    return count
    
    
def generate_binary_iter(n):
    total = 0
    for i in range(2 ** n):
        binary_str = f"{i:0{n}b}"  # format i as n-bit binary string
        print(binary_str)
        total += 1
    return total


    
def main():
    total = generate_binary(2)
    print(f"Total number of combinations:", total)
    print()
    total = generate_binary_iter(2)
    print(f"Total number of combinations:", total)
    
     
if __name__ == "__main__":
    main()