def main():
    print(getNthFibNaive(7))
    print(getNthFibSoSo(7))
    print(getNthFib(7))
    print(detNthFib_best(7))
    
def getNthFibNaive(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    return getNthFibNaive(n - 2) + getNthFibNaive(n - 1)

# O(n) time | O(n) space
def getNthFibSoSo(n):
    arr = [None] * (n + 1)
    arr[0] = 0
    arr[1] = 1
    
    for i in range(2, n + 1):
        arr[i] = arr[i - 2] + arr[i - 1]
        
    return arr[n]

# O(n) time | O(1) space
def getNthFib(n):
    if n == 1:
        return 0
    arr = [0, 1]
    counter = 2
    while counter <= n:
        newValue = arr[0] + arr[1]
        arr[0] = arr[1]
        arr[1] = newValue
        counter += 1
    return arr[1]

# O(n) time | O(1) space
def detNthFib_best(n):
    first, second = 0, 1
    for _ in range(n):
        third = first + second
        first = second
        second = third
    return first
    
    

if __name__ == "__main__":
    main()