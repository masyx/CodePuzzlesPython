def main():
    print(getNthFib(1))
    
def getNthFibNaive(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    
    return getNthFibNaive(n - 2) + getNthFibNaive(n - 1)

# O(n) time | O(n) space
def getNthFib(n):
    arr = [None] * (n + 2)
    arr[1] = 0
    arr[2] = 1
    
    for i in range(3, n + 1):
        arr[i] = arr[i - 2] + arr[i - 1]
        
    return arr[n]
    
    

if __name__ == "__main__":
    main()