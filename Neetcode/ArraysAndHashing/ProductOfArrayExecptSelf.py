# O(n^2) time | O(n) space
def productExceptSelf_bruteForce(lst):
    left_product = 1
    result = [0] * len(lst)
    for i in range(len(lst)):
        current_product = 1
        for j in range(i + 1, len(lst)):
            current_product *= lst[j]
        result[i] = current_product * left_product
        left_product = left_product * lst[i]
    return result

# O(n) time | O(n) space
def productExceptSelf_extraSpace(lst):
    prefixProduct = [1] * len(lst)
    suffixProduct = [1] * len(lst)
    result = [0] * len(lst)
    for i in range(1, len(lst)):
        prefixProduct[i] = prefixProduct[i - 1] * lst[i - 1]
    for i in range(len(lst) - 2, -1 , -1):
        suffixProduct[i] = suffixProduct[i + 1] * lst[i + 1]
    for i in range(len(lst)):
        result[i] = prefixProduct[i] * suffixProduct[i]
    return result
    
# O(n) time | O(1) space
def productExceptSelf(lst):
    result = []
    left = 1
    for elem in lst:
        result.append(left)
        left *= elem
    right = 1
    for i in reversed(range(len(lst))):
        result[i] *= right
        right *= lst[i]
    return result

# O(n) time | O(1) space
def productExceptSelf_2(lst):
    result = [1] * len(lst)
    for i in range(1, len(lst)):
        result[i] = result[i - 1] * lst[i - 1]
    right = 1
    for i in reversed(range(len(lst))):
        result[i] *= right
        right *= lst[i]
    return result


def main():
    my_ints = [2,3,8,2,10]
    print(productExceptSelf_extraSpace(my_ints))
    print(productExceptSelf(my_ints))
    print(productExceptSelf_2(my_ints))
    
if __name__ == "__main__":
    main()