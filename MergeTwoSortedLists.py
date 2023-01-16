# O(n + m ) time
# O(n + m) space
def merge_lists(lst1, lst2):
    idx_1 = idx_2 = idx_res = 0
    
    result = [i for i in range(len(lst1) + len(lst2))]
    
    while idx_1 < len(lst1) and idx_2 < len(lst2):
        if lst1[idx_1] < lst2[idx_2]:
            result[idx_res] = lst1[idx_1]
            idx_1 += 1
            idx_res += 1
        else:
            result[idx_res] = lst2[idx_2]
            idx_2 += 1
            idx_res += 1
    while idx_1 < len(lst1):
        result[idx_res] = lst1[idx_1]
        idx_1 += 1
        idx_res += 1
    while idx_2 < len(lst2):
        result[idx_res] = lst2[idx_2]
        idx_2 += 1
        idx_res += 1
    return result


def main():
    lst1 = [1,2,3,10]
    lst2 = [2,5,6]
    new_list = merge_lists(lst1, lst2)
    print(new_list)
    
    
if __name__ == "__main__":
    main()