def getNthFibRec(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    return getNthFib(n - 2) + getNthFib(n - 1)

def getNthFib(n):
    arr = [0, 1]
    counter = 3
    while counter <= n:
        nextValue = sum(arr)
        arr[0] = arr[1]
        arr[1] = nextValue
        counter += 1
    return arr[1] if n > 1 else arr[0]



def main():
    print(getNthFib(5))
    
if __name__ == "__main__":
    main()