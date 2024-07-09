def merge_sorted_array(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    if arr1[0] < arr2[0]:
        res = merge_sorted_array(arr1[1:], arr2)
        merged_arr = [arr1[0]] + res
        return merged_arr
    else:
        res = merge_sorted_array(arr1, arr2[1:])
        merged_arr = [arr2[0]] + res
        return merged_arr


if __name__ == "__main__":
    arr1 = [0, 2, 4]
    arr2 = [1, 3]
    print(merge_sorted_array(arr1, arr2))