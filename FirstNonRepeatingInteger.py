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
    """
    This function takes a list of elements as input (lst) and returns the first unique element
    in the list. It does so by creating a dictionary (counts) to keep track of the number of 
    occurrences of each element in the list. It then iterates through the list, checking if 
    the count of an element in the dictionary is equal to 1. If it is, the function 
    returns that element. If no unique element is found, the function returns None.
    """
    counts = {}
    for elem in lst:
        counts[elem] = counts.get(elem, 0) + 1
    for elem in lst:
        if counts[elem] == 1:
            return elem
    return None


def find_first_unique_short(lst):
    numbers = {}
    for elem in lst:
        numbers[elem] = numbers.get(elem, 0) + 1
    return next((elem for elem in lst if numbers[elem] == 1), None)

def main():
    print(find_first_unique_BF_1([9,2,3,3,9,6]))
    print(find_first_unique_BF_1([9,2,3,2,6,6]))
    print(find_first_unique_BF_1([4,5,1,5,4]))
    print(find_first_unique_BF_1([0,0]))
    print()
    print(find_first_unique_short([9,2,3,3,9,6]))
    print(find_first_unique_short([9,2,3,2,6,6]))
    print(find_first_unique_short([4,5,1,5,4]))
    print(find_first_unique_short([0,0]))
    
    
    
    
if __name__ == "__main__":
    main()