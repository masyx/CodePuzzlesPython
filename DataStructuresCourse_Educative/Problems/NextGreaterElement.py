
# O(n^2) time |O(1) space
def next_greater_element_brute_force(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[i]:
                result.append(lst[j])
                break
            if j == len(lst) - 1:
                # if there is no value greater than str[i]
                result.append(-1)
        
    result.append(-1)
    return result

# lst = [2, 9, 0, 22]
# result: [9, 22, 22, -1]
# O(n) time | O(1) space
def next_greater_element(lst):
    stack = [] # to track the seen elements
    result = [-1] * len(lst)
    
    for i, element in enumerate(lst):
        while stack and element > lst[stack[-1]]:
            result[stack.pop()] = element
        stack.append(i)
    return result



if __name__ == "__main__":
    lst = [2, 9, 0, 22]
    # result: [9, 22, 22, -1]
    
    print(next_greater_element(lst))