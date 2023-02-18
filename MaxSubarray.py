def maxSubArray(lst) -> int:
    if len(lst) == 1:
        return lst[0]
    max_sum = float('-inf')
    for i in range(len(lst)):
        current = lst[i]
        for j in range(i + 1, len(lst)):
            current += lst[j]
            max_sum = max(max_sum, current)
    return max_sum


def main():
    lst = [-10,10,7,-5,15,-20]
    print(maxSubArray(lst))
    
if __name__ == "__main__":
    main()