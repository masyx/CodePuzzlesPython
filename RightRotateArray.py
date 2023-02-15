# O(n) time | O(n) space
def right_rotate(lst, k):
    if len(lst) == 0:
        return None
    rotated_lst = [0] * len(lst)
    for i in range(len(lst)):
        rotated_lst[(i + k) % len(lst)] = lst[i]
    # lst[:] = rotated_lst if needed in place
    return rotated_lst


 # O(n) time | O(1) space | Pythonic solution
def right_rotate_2(lst, k):
    if len(lst) == 0:
        return
    else:
        k = k % len(lst) 
    lst[:] = lst[-k:] + lst[:-k]


# O(n x k) which is O(n) | O(1) space
def right_rotate_in_place_brute(lst, k):
    k %= len(lst)
    for i in range(k):
        previous = lst[-1]
        for j in range(len(lst)):
            # tmp = lst[j] # not pythonic way
            # lst[j] = previous
            # previous = tmp
            lst[j], previous = previous, lst[j]


def main():
    lst = [10,20,30,40,50]
    k = 1
    
    print(f"Original list: {lst}")

    right_rotate_in_place_brute(lst, k)
    print("Rotated list:", lst)


if __name__ == "__main__":
    main()