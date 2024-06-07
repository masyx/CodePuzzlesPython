def sort_colors(colors):
    return colors

def sort_colors_counting(colors):
    count = [0, 0, 0]
    
    # Count the occurrences of each color
    for color in colors:
        count[color] += 1
    
    index = 0
    for color in range(3):
        for _ in range(count[color]):
            colors[index] = color
            index += 1
    return colors

def sort_colors_counting_generic(nums):
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    counts = dict(sorted(counts.items()))
    index = 0
    for key in counts.keys():
        for _ in range(counts[key]):
            nums[index] = key
            index += 1
    return nums

def main():
    #colors = [2, 1, 0, 3]
    colors = [2, 1, 4, 2, 1, 4, 4, 1, 1, 2, 2, 1, 1, 4]
    print(sort_colors_counting_generic(colors))
    

if __name__ == "__main__":
    main()