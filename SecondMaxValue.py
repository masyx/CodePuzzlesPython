# O(n) time | O(1) space
def find_second_maximum(lst):
    """
    The code defines a function called find_second_maximum that takes a list lst as input. 
    The function first checks if the length of the list is less than 2. If it is, the function returns None 
    because it is not possible to find the second maximum number in a list with less than 2 elements.
    If the list has at least 2 elements, the function initializes two variables, first_max and second_max, 
    to negative infinity. The function then iterates over each number in the list. If the current number 
    is greater than the current first_max, it updates first_max to be equal to the current number and 
    second_max to be equal to the previous value of first_max. If the current number is greater than 
    second_max but not equal to first_max, the function updates second_max to be equal to the current number.
    Finally, the function returns second_max if it is not equal to negative infinity, otherwise it returns None.
    """
    if len(lst) < 2:
        return None
    first_max = second_max = float("-inf")
    for num in lst:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num
    return second_max if second_max != float("-inf") else None


# O(n) time | O(1) space
def find_second_maximum_2iterations(lst):
    if len(lst) < 2:
        return None
    first_max = float("-inf")
    second_max = float("-inf")
    for num in lst:
        if num > first_max:
            first_max = num
            
    for num in lst:
        if num != first_max and num > second_max:
            second_max = num
    return second_max if second_max != float("-inf") else None

# O(n log n) time | O(1) space
def find_second_maximum_sort(lst):
    lst.sort()
    if len(lst) > 1:
        return lst[-2]
    else:
        return None



def main():
    lst1 = [9,2,3,6]
    lst2 = [2,4,1,5,0]
    print(find_second_maximum([9,2,3,6]))
    
if __name__ == "__main__":
    main()