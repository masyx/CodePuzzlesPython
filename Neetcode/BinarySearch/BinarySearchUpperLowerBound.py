# Lower Bound - the index of the first element that is greater than or equal to the target
# Upper Bound - the index of the first element that is strictly greater than the target
#i 0 1 2 3 4 5
# [2,3,3,4,6,8], target = 2
# l = 0, r = 5, mid = 2
def lower_bound(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        # this condition is based on the lower bound definition
        # given above
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l


def upper_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        # this condition is based on the upper bound definition 
        # given above
        if nums[mid] > target:
            r = mid
        else:
            l = mid + 1
    return l


def main():
    nums = [2,3,3,4,6,8]
    target = 3
    print(lower_bound(nums, target))
    print(upper_bound(nums, target))


if __name__ == "__main__":
    main()
