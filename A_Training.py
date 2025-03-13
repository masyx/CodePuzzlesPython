#  i    0  1  2   3
# arr  [2, 5,  3, 4]
# pre  [1, 2, 10,30]
# post [60,12, 4, 1]
# res  [60,24,40,30]

# O(n) time | O(n) space
def product_except_self(nums):
    answer = [1] * len(nums)
    pre_prod = [1] * len(nums)
    post_prod = [1] * len(nums)
    
    for i in range(1, len(nums)):
        pre_prod[i] = pre_prod[i - 1] * nums[i - 1]
    
    for i in range(len(nums) - 2, -1, -1):
        post_prod[i] = post_prod[i + 1] * nums[i + 1]
        
    for i in range(len(answer)):
        answer[i] = pre_prod[i] * post_prod[i]
    
    return answer

        


def main():
    nums = [2, 5, 3, 4]
    print(product_except_self(nums))
    
     
if __name__ == "__main__":
    main()