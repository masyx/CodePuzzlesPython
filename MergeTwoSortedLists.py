# O(n) time, where n is length of the longest list
# O(n + m) space
def merge_lists(lst1, lst2):
    idx_1 = idx_2 = 0
    result = []
    while idx_1 < len(lst1) and idx_2 < len(lst2):
        if lst1[idx_1] < lst2[idx_2]:
            result.append(lst1[idx_1])
            idx_1 += 1
        else:
            result.append(lst2[idx_2])
            idx_2 += 1
    while idx_1 < len(lst1):
        result.append(lst1[idx_1])
        idx_1 += 1
    while idx_2 < len(lst2):
        result.append(lst2[idx_2])
        idx_2 += 1
    return result


def main():
    lst1 = [1,2,3,10]
    lst2 = [2,5,6]
    new_list = merge_lists(lst1, lst2)
    print(new_list)
    
    
if __name__ == "__main__":
    main()