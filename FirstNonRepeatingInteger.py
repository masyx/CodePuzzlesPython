# O(n^2) time | O(1) space
def find_first_unique_BF_1(lst: list):
    for elem in lst:
        if lst.count(elem) == 1:
            return elem
    return None

# O(n^2) time | O(1) space
def find_first_unique_BF_2(lst):
    for i in range(len(lst)):
        is_unique = True
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                is_unique = False
                break
        if is_unique:
            return lst[i]
    return None

# O(n) time | O(n) space
def find_first_unique(lst: list):
    counts = {}
    for elem in lst:
        counts[elem] = counts.get(elem, 0) + 1
    # for key, value in counts.items():
    #     if value == 1:
    #         return key
    for elem in lst:
        if counts[elem] == 1:
            return elem
    return None

def main():
    print(find_first_unique_BF_1([9,2,3,3,9,6]))
    print(find_first_unique_BF_1([9,2,3,2,6,6]))
    print(find_first_unique_BF_1([4,5,1,5,4]))
    print(find_first_unique_BF_1([0,0]))
    print()
    print(find_first_unique([9,2,3,3,9,6]))
    print(find_first_unique([9,2,3,2,6,6]))
    print(find_first_unique([4,5,1,5,4]))
    print(find_first_unique([0,0]))
    
    
    
    
if __name__ == "__main__":
    main()