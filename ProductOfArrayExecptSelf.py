# O(n^2) time | O(n) space
def productExceptSelf(lst):
    left_product = 1
    result = [0] * len(lst)
    for i in range(len(lst)):
        current_product = 1
        for j in range(i + 1, len(lst)):
            current_product *= lst[j]
        result[i] = current_product * left_product
        left_product = left_product * lst[i]
    return result
        
    
    
def main():
    my_ints = [1,2,3,4]
    print(productExceptSelf(my_ints))
    
if __name__ == "__main__":
    main()