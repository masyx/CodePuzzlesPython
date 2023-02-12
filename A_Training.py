# O(n) time | O(n) space
def right_rotate(lst, k):
    if len(lst) == 0:
        return None
    rotated_lst = [0] * len(lst)
    for i in range(len(lst)):
        rotated_lst[(i + k) % len(lst)] = lst[i]
    return rotated_lst

 # O(n) time | O(n) space | Pythonic solution
def right_rotate_2(lst, k):
    if len(lst) == 0:
        return None
    else:
        k = k % len(lst) 
    return lst[-k:] + lst[:-k]


def main():
    lst = [10,20,30,40,50]
    k = 1
    
    print(lst)
    print(right_rotate(lst, k))
    
    
if __name__ == "__main__":
    main()