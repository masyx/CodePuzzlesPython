def find_first_unique(lst: list):
    for elem in lst:
        if lst.count(elem) == 1:
            return elem
    return None


def first_unique_int(lst):
    for i in range(len(lst)):
        is_unique = True
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                is_unique = False
                break
        if is_unique:
            return lst[i]
    return None


def main():
    print(find_first_unique([9,2,3,3,9,6]))
    print(find_first_unique([9,2,3,2,6,6]))
    print(find_first_unique([4,5,1,5,4]))
    print(find_first_unique([0,0]))
    print()
    print(first_unique_int([9,2,3,3,9,6]))
    print(first_unique_int([9,2,3,2,6,6]))
    print(first_unique_int([4,5,1,5,4]))
    print(first_unique_int([0,0]))
    
    
    
    
if __name__ == "__main__":
    main()