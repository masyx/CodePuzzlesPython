def search(nums, target) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1
    

def search_req(nums, target: int) -> int:
    l = 0
    r = len(nums) - 1
    m = (l + r) // 2
    if nums[m] == target:
        return m
    if nums[m] < target:
        search_req(nums[m + 1:], target)
    else:
        search_req(nums[:m - 1], target)
    return - 1
        
            

if __name__ == "__main__":
    prices = [1, 3, 5, 7, 9, 12]
    print(search_req(prices, 13))