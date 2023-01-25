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
def productExceptSelf(lst):
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
    
def main():
    my_ints = [5,2,3,4]
    print(productExceptSelf(my_ints))
    
if __name__ == "__main__":
    main()