# Given an unsorted array of numbers and a target ‘key’, remove all 
# instances of ‘key’ in-place and return the new length of the array.

# O(n) time | O(1) space
def remove_key(arr, key):
    new_arr_start_index = 0
    for i in range(len(arr)):
        if arr[i] == key:
            arr[new_arr_start_index], arr[i] = arr[i], arr[new_arr_start_index]
            new_arr_start_index += 1
    return len(arr) - new_arr_start_index


def remove_key_2(arr, key):
    next_not_key_element = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_not_key_element] = arr[i]
            next_not_key_element += 1
    return next_not_key_element

def main():
    arr = [2, 11, 2, 2, 1]
    key = 2
    print(remove_key(arr, key))
    
    
if __name__ == "__main__":
    main()