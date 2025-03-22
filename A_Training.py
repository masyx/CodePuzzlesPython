

def max_area_bf(height):
    if not height:
        return 0
    res = 0
    for i in range(len(height)):
        for j in range(len(height)):
            res = max(res, min(height[i], height[j]) * (j - i))
    return res

def max_area(height):
    if not height:
        return 0
    res = 0
    l = 0
    r = len(height) - 1
    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res


def main():
    #i:0 1 2 3 4 5 6 7 8
    # [1,8,6,2,5,4,8,3,7]
    height = [1,8,6,2,5,4,8,3,7]
    print(max_area_bf(height))
    print(max_area(height))
    
     
if __name__ == "__main__":
    main()