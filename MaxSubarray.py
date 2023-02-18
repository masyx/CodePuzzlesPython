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


def maxSubArray_Kadanes(lst):
    curr_max = global_max = lst[0]
    for i in range(1, len(lst)):
        if curr_max < 0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]
        global_max = max(curr_max, global_max)
    return global_max

def main():
    lst = [-10,10,7,-5,15,-20]
    print(maxSubArray(lst))
    print(maxSubArray_Kadanes(lst))
    
if __name__ == "__main__":
    main()