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

# O(nm) space, don't know why tbh
# O(m) space, where m is the length of second list
def merge_lists_inplace(lst1: list, lst2):
    idx1 = idx2 = 0
    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1] < lst2[idx2]:
            idx1 += 1
        else:
            lst1.insert(idx1, lst2[idx2])
            idx1 += 1
            idx2 += 1
    if idx2 < len(lst2):
        lst1.extend(lst2[idx2:])
    return lst1


def main():
    lst1 = [1,2,3,10]
    lst2 = [2,5,6]
    new_list = merge_lists(lst1, lst2)
    print(new_list)
    
    lst3 = [4, 5, 6]
    lst4 = [7,8,9]
    new_list_2 = merge_lists_inplace(lst3, lst4)
    print(new_list_2)
    
    
if __name__ == "__main__":
    main()