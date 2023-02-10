# O(n) time | O(n) space
def right_rotate(lst, k):
    if len(lst) == 0:
        return None
    rotated_lst = [0] * len(lst)
    for i in range(len(lst)):
        rotated_lst[(i + k) % len(lst)] = lst[i]
    return rotated_lst


def main():
    lst = [10,20,30,40,50]
    k = 33
    
    print(lst)
    print(right_rotate(lst, k))
    
    
if __name__ == "__main__":
    main()