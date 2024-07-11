# O(n + m) time | O(n + m) space, for recursive calls and result array
def merge_sorted_arrays(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    if arr1[0] < arr2[0]:
        merged_arr = merge_sorted_arrays(arr1[1:], arr2)
        result_arr = [arr1[0]] + merged_arr
        return result_arr
    else:
        return [arr2[0]] + merge_sorted_arrays(arr1, arr2[1:])

# O(n + m) time | O(n + m) space
def merge_sorted_arrays_iterative(arr1, arr2):
    result_arr = [None for i in range(len(arr1) + len(arr2))]
    #result_arr = [None] * (len(arr1) + len(arr2))
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result_arr[k] = arr1[i]
            i += 1
        else:
            result_arr[k] = arr2[j]
            j += 1
        k += 1
        
    while i < len(arr1):
        result_arr[k] = arr1[i]
        i += 1
        k += 1
        
    while j < len(arr2):
        result_arr[k] = arr2[j]
        j += 1
        k += 1
        
    return result_arr 

def merge_sorted_arrays_iterative_pythonic(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def mergeTwoSortedLinkedLists(head1, head2):
    pre_head = Node(-1)
    current = pre_head
    
    while head1 and head2:
        if head1.value < head2.value:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
        
    current.next = head1 or head2
    return pre_head.next


if __name__ == "__main__":
    arr1 = [0, 2]
    arr2 = [1, 3, 5]
    print(merge_sorted_arrays(arr1, arr2))
    print(merge_sorted_arrays_iterative(arr1, arr2))
    print(merge_sorted_arrays_iterative_pythonic(arr1, arr2))
